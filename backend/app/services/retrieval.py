from typing import List, Dict, Any
from app.services.embeddings import EmbeddingService
from app.services.local_vector_store import vector_store

class RetrievalService:
    def __init__(self, embedding_service: EmbeddingService):
        self.embedding_service = embedding_service

    def hybrid_search(self, query: str, repo_id: str, query_emb: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        # Get semantic results
        semantic_results = vector_store.search(repo_id, query_emb, limit=2000)
        
        import re
        clean_query = re.sub(r'[^\w\s_]', '', query.lower())
        query_words = set(clean_query.split())
        scored_results = []
        
        for sim_score, point in semantic_results:
            chunk = point["metadata"]
            source_code = chunk.get("source_code", "").lower()
            symbol_name = chunk.get("symbol_name", "").lower()
            
            # Keyword score (ignore short common words)
            keyword_matches = sum(1 for w in query_words if len(w) > 3 and w in source_code)
            keyword_score = keyword_matches / max(len(query_words), 1)
            
            # Symbol name match (MASSIVE BOOST)
            symbol_score = sum(2.0 for w in query_words if len(w) > 2 and w in symbol_name)
            
            # Exact phrase match boost
            exact_match_score = 2.0 if symbol_name and symbol_name in clean_query else 0.0
            
            # Structural score
            structural_score = 0.0
            if chunk.get("symbol_type") in ["class", "function", "method"]:
                structural_score = 1.0
            
            # Hybrid score with high weight on symbol matches
            hybrid_score = (0.1 * sim_score) + (1.0 * keyword_score) + (0.5 * structural_score) + symbol_score + exact_match_score
            
            scored_results.append((hybrid_score, chunk))
            
        scored_results.sort(key=lambda x: x[0], reverse=True)
        return [res[1] for res in scored_results[:limit]]
