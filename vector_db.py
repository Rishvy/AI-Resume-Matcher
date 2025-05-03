import faiss
import numpy as np
import os
import json

embedding_dim = 384
resume_index_path = "data/resume_embeddings.index"
job_index_path = "data/job_embeddings.index"

# Initialize or load FAISS index
def load_faiss_index(path):
    if os.path.exists(path):
        return faiss.read_index(path)
    else:
        return faiss.IndexFlatL2(embedding_dim)

# Save embedding with metadata
def save_embedding(index_path, embedding, metadata_path, metadata):
    index = load_faiss_index(index_path)
    index.add(np.array([embedding], dtype=np.float32))
    faiss.write_index(index, index_path)

    os.makedirs(os.path.dirname(metadata_path), exist_ok=True)
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(metadata)
    with open(metadata_path, "w") as f:
        json.dump(existing, f, indent=2)