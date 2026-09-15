import math
import sqlite3
import json
import os
from typing import List, Dict, Any, Tuple

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "data", "codebase_ai.db")

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm_a = math.sqrt(sum(a * a for a in vec1))
    norm_b = math.sqrt(sum(b * b for b in vec2))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

class LocalVectorStore:
    def __init__(self):
        self._init_db()

    def _get_connection(self):
        return sqlite3.connect(DB_PATH)

    def _init_db(self):
        conn = self._get_connection()
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS vector_chunks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chunk_id TEXT,
                repository_id TEXT,
                embedding TEXT,
                metadata TEXT
            )
        """)
        c.execute("CREATE INDEX IF NOT EXISTS idx_vector_repo ON vector_chunks(repository_id)")
        conn.commit()
        conn.close()

    def upsert(self, chunk_id: str, repository_id: str, embedding: List[float], metadata: Dict[str, Any]):
        conn = self._get_connection()
        c = conn.cursor()
        c.execute("""
            INSERT INTO vector_chunks (chunk_id, repository_id, embedding, metadata)
            VALUES (?, ?, ?, ?)
        """, (chunk_id, repository_id, json.dumps(embedding), json.dumps(metadata)))
        conn.commit()
        conn.close()

    def upsert_batch(self, chunks: List[Tuple[str, str, List[float], Dict[str, Any]]]):
        conn = self._get_connection()
        c = conn.cursor()
        batch_data = [
            (chunk_id, repository_id, json.dumps(embedding), json.dumps(metadata))
            for chunk_id, repository_id, embedding, metadata in chunks
        ]
        c.executemany("""
            INSERT INTO vector_chunks (chunk_id, repository_id, embedding, metadata)
            VALUES (?, ?, ?, ?)
        """, batch_data)
        conn.commit()
        conn.close()

    def delete_repository(self, repository_id: str):
        conn = self._get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM vector_chunks WHERE repository_id=?", (repository_id,))
        conn.commit()
        conn.close()

    def clear(self):
        conn = self._get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM vector_chunks")
        conn.commit()
        conn.close()

    def search(self, repository_id: str, query_embedding: List[float], limit: int = 5) -> List[Tuple[float, Dict[str, Any]]]:
        conn = self._get_connection()
        c = conn.cursor()
        c.execute("SELECT chunk_id, embedding, metadata FROM vector_chunks WHERE repository_id=?", (repository_id,))
        
        results = []
        for row in c.fetchall():
            chunk_id, emb_str, meta_str = row
            embedding = json.loads(emb_str)
            metadata = json.loads(meta_str)
            
            score = cosine_similarity(query_embedding, embedding)
            results.append((score, {
                "chunk_id": chunk_id,
                "repository_id": repository_id,
                "embedding": embedding,
                "metadata": metadata
            }))
        
        conn.close()
        results.sort(key=lambda x: x[0], reverse=True)
        return results[:limit]

# Singleton instance
vector_store = LocalVectorStore()
