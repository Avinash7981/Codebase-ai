import hashlib
from typing import List

try:
    from sentence_transformers import SentenceTransformer
    HAS_BGE = True
except ImportError:
    HAS_BGE = False

class EmbeddingService:
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.is_fallback = not HAS_BGE
        if HAS_BGE:
            self.model = SentenceTransformer(model_name)
        else:
            print("WARNING: BGE unavailable. Using deterministic local fallback.")

    def generate_embedding(self, text: str) -> List[float]:
        """Generates a single embedding for a given text."""
        if self.is_fallback:
            # Deterministic fallback embedding based on text hash
            h = int(hashlib.sha256(text.encode('utf-8')).hexdigest(), 16)
            vec = [(h >> i & 1) * 0.1 for i in range(384)]
            return vec
            
        return self.model.encode(text, normalize_embeddings=True).tolist()

    def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generates embeddings for a batch of texts."""
        if self.is_fallback:
            return [self.generate_embedding(t) for t in texts]
            
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        return [emb.tolist() for emb in embeddings]
