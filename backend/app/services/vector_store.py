from __future__ import annotations

import faiss
import numpy as np


class FaissStore:
    def __init__(self, vector_dim: int):
        self.index = faiss.IndexFlatIP(vector_dim)
        self.ids: list[int] = []

    def add(self, entity_id: int, embedding: list[float]) -> None:
        vector = np.array([embedding], dtype="float32")
        self.index.add(vector)
        self.ids.append(entity_id)

    def search(self, embedding: list[float], top_k: int = 5) -> list[tuple[int, float]]:
        if self.index.ntotal == 0:
            return []
        query = np.array([embedding], dtype="float32")
        scores, positions = self.index.search(query, top_k)

        results = []
        for score, pos in zip(scores[0], positions[0]):
            if pos == -1:
                continue
            results.append((self.ids[pos], float(score)))
        return results
