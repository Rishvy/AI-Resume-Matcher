import numpy as np
from backend.vector_db import load_faiss_index, get_job_metadata

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def match_jobs(resume_embedding, top_k=5):
    job_index = load_faiss_index("data/job_embeddings.index")
    distances, indices = job_index.search(np.array([resume_embedding], dtype=np.float32), k=top_k)
    job_matches = []
    for idx, dist in zip(indices[0], distances[0]):
        metadata = get_job_metadata(idx)
        similarity = 1 - dist  # Since FAISS uses L2 distance
        job_matches.append({
            "job": metadata,
            "similarity": similarity
        })
    return sorted(job_matches, key=lambda x: x["similarity"], reverse=True)