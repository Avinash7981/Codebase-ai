from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from typing import List, Dict, Any
from app.core.config import settings
import os

class QdrantService:
    def __init__(self):
        if settings.QDRANT_URL:
            self.client = QdrantClient(url=settings.QDRANT_URL)
        else:
            os.makedirs(settings.QDRANT_PATH, exist_ok=True)
            self.client = QdrantClient(path=settings.QDRANT_PATH)
            
        self.collection_name = "codebase_chunks"
        self._ensure_collection()

    def _ensure_collection(self):
        try:
            collections = self.client.get_collections().collections
            if not any(c.name == self.collection_name for c in collections):
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
                )
        except Exception as e:
            print(f"Error ensuring Qdrant collection: {e}")

    def insert_chunks(self, chunks: List[Dict[str, Any]], embeddings: List[List[float]]):
        points = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            payload = chunk.copy()
            point_id = payload.pop("chunk_id") # Use chunk_id as point ID if it's a valid UUID
            
            points.append(PointStruct(
                id=point_id,
                vector=embedding,
                payload=payload
            ))
            
        if points:
            self.client.upsert(
                collection_name=self.collection_name,
                points=points
            )

    def search(self, query_embedding: List[float], repo_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="repository_id",
                        match=MatchValue(value=repo_id)
                    )
                ]
            ),
            limit=limit
        )
        
        results = []
        for hit in search_result:
            chunk_data = hit.payload
            chunk_data["chunk_id"] = hit.id
            chunk_data["score"] = hit.score
            results.append(chunk_data)
            
        return results
