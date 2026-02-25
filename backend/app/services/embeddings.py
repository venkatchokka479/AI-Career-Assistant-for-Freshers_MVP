import threading

import numpy as np
from sentence_transformers import SentenceTransformer

from app.core.config import settings


class EmbeddingService:
    _model: SentenceTransformer | None = None
    _lock = threading.Lock()

    @classmethod
    def model(cls) -> SentenceTransformer:
        if cls._model is None:
            with cls._lock:
                if cls._model is None:
                    cls._model = SentenceTransformer(settings.embedding_model)
        return cls._model

    @classmethod
    def embed_text(cls, text: str) -> np.ndarray:
        vector = cls.model().encode([text], normalize_embeddings=True)
        return vector[0]


def cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    denominator = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    if denominator == 0:
        return 0.0
    return float(np.dot(vec_a, vec_b) / denominator)
