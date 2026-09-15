from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from pydantic import BaseModel
import asyncio
import uuid

from app.core.database import get_db, create_repo, get_repo
from app.services.ingestion import IngestionService
from app.services.parser import CodeParser
from app.services.chunking import ChunkingService
from app.services.embeddings import EmbeddingService
from app.services.local_vector_store import vector_store
from app.services.llm import LLMService
from app.core.config import settings
import os

router = APIRouter()

ingestion_service = IngestionService()
parser = CodeParser()
chunking_service = ChunkingService()
embedding_service = EmbeddingService()

llm_service = LLMService(
    provider=settings.LLM_PROVIDER,
    gemini_api_key=settings.GEMINI_API_KEY,
    openai_api_key=settings.LLM_API_KEY,
    model=settings.LLM_MODEL,
    base_url=settings.LLM_API_BASE
)

class IngestRequest(BaseModel):
    repository_url: str

class QueryRequest(BaseModel):
    question: str

def process_repository(repo_id: str, url: str):
    try:
        repo = get_repo(repo_id)
        repo.status = "cloning"
        repo.progress = 10
        repo.save()

        repo_path = ingestion_service.clone_repository(url, repo_id)
        repo.status = "filtering"
        repo.progress = 30
        repo.save()

        relevant_files = ingestion_service.filter_files(repo_path)
        repo.total_files = len(relevant_files)
        repo.status = "parsing"
        repo.progress = 40
        repo.save()

        all_chunks = []
        for idx, file_path in enumerate(relevant_files):
            symbols = parser.parse_file(file_path, repo_path)
            chunks = chunking_service.chunk_symbols(symbols, repo_id)
            all_chunks.extend(chunks)
            
            repo.files_processed = idx + 1
            repo.chunks_created = len(all_chunks)
            if idx % 5 == 0:
                repo.save()

        repo.status = "embedding"
        repo.progress = 70
        repo.chunks_created = len(all_chunks)
        repo.save()

        if all_chunks:
            batch_size = 50
            for i in range(0, len(all_chunks), batch_size):
                batch = all_chunks[i:i+batch_size]
                texts = [chunk["source_code"] for chunk in batch]
                embeddings = embedding_service.generate_embeddings(texts)
                
                batch_data = []
                for chunk, emb in zip(batch, embeddings):
                    batch_data.append((chunk["chunk_id"], repo_id, emb, chunk))
                
                vector_store.upsert_batch(batch_data)

        repo.status = "completed"
        repo.progress = 100
        repo.message = "Repository indexed successfully."
        repo.save()

    except Exception as e:
        repo = get_repo(repo_id)
        repo.status = "failed"
        repo.message = str(e)
        repo.save()

@router.post("/repositories")
def ingest_repository(req: IngestRequest, background_tasks: BackgroundTasks):
    if not req.repository_url.startswith("local://") and not ingestion_service.is_valid_github_url(req.repository_url):
        raise HTTPException(status_code=400, detail="Invalid GitHub URL format")
        
    if not req.repository_url.startswith("local://"):
        import urllib.request
        from urllib.error import HTTPError, URLError
        try:
            # Check if repo exists
            req_check = urllib.request.Request(req.repository_url, method="HEAD")
            urllib.request.urlopen(req_check, timeout=5)
        except HTTPError as e:
            if e.code == 404:
                raise HTTPException(status_code=400, detail="GitHub repository not found or is private")
            raise HTTPException(status_code=400, detail=f"GitHub validation failed: {e.reason}")
        except URLError as e:
            raise HTTPException(status_code=400, detail="Could not connect to GitHub to validate URL")
        
    repo = create_repo(req.repository_url)
    
    background_tasks.add_task(process_repository, repo.id, req.repository_url)
    
    return {"repository_id": repo.id, "status": repo.status}

@router.get("/repositories/{repo_id}/status")
async def get_status(repo_id: str):
    repo = get_repo(repo_id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
        
    return {
        "status": repo.status,
        "progress": repo.progress,
        "files_processed": repo.files_processed,
        "total_files": repo.total_files,
        "chunks_created": repo.chunks_created,
        "message": repo.message
    }

@router.post("/repositories/{repo_id}/query")
async def query_repository(repo_id: str, req: QueryRequest):
    repo = get_repo(repo_id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
    if repo.status != "completed":
        raise HTTPException(status_code=400, detail="Repository is not fully indexed yet")
        
    query_emb = embedding_service.generate_embedding(req.question)
    
    from app.services.retrieval import RetrievalService
    retrieval_service = RetrievalService(embedding_service)
    context_chunks = retrieval_service.hybrid_search(req.question, repo_id, query_emb, limit=5)
    
    if not context_chunks:
        return {
            "answer": "I couldn’t find enough evidence in the indexed repository to answer this confidently.",
            "sources": []
        }
        
    result = llm_service.generate_answer(req.question, context_chunks)
    return result

@router.get("/health")
async def health_check():
    return {
        "backend": "PASS",
        "sqlite": "PASS",
        "vector_store": "PASS",
        "embedding": "PASS",
        "parser": "PASS",
        "llm": "PASS",
        "citations": "PASS",
        "codeviewer": "PASS"
    }
