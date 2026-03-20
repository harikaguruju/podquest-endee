import json
import numpy as np
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from .config import EMBEDDING_MODEL

# Load saved embeddings and metadata
def load_data():
    embeddings = np.load("endee_embeddings.npy")
    with open("endee_metadata.json", "r") as f:
        metadata = json.load(f)
    return embeddings, metadata

# Cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Search function
def search(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    embeddings, metadata = load_data()

    model = SentenceTransformer(EMBEDDING_MODEL)

    # Convert query to embedding
    query_emb = model.encode(query, convert_to_numpy=True, normalize_embeddings=True)

    # Compute similarity
    scores = []
    for i, emb in enumerate(embeddings):
        sim = cosine_similarity(query_emb, emb)
        scores.append((sim, i))

    # Sort by similarity
    scores = sorted(scores, reverse=True, key=lambda x: x[0])

    # Get top results
    results = []
    for score, idx in scores[:top_k]:
        item = metadata[idx]
        item["score"] = float(score)
        results.append(item)

    return results
