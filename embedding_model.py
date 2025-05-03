from sentence_transformers import SentenceTransformer

# Load a sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str):
    return model.encode(text, show_progress_bar=False)