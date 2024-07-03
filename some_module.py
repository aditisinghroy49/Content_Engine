import os
from typing import List
from chromadb.api.client import Client
from sentence_transformers import SentenceTransformer

def parse_pdf() -> tuple:
    pdfs_dir = os.path.join(os.getcwd(), 'pdfs')
    texts = []
    vectors = []
    for filename in os.listdir(pdfs_dir):
        if filename.endswith('.pdf'):
            text, vector = process_pdf(os.path.join(pdfs_dir, filename))
            texts.append(text)
            vectors.append(vector)
    return vectors, texts

def process_pdf(pdf_file: str) -> tuple:
    # Replace this with your actual PDF processing logic
    text = "Sample text from PDF"
    vector = [0.1, 0.2, 0.3]  # Example vector, replace with actual vector
    return text, vector

def generate_vectors(texts: List[str]) -> List[list]:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    vectors = [model.encode(text) for text in texts]
    return vectors

def store_vectors(vectors: List[list], texts: List[str]) -> object:
    client = Client()
    collection = client.create_collection("document_collection")
    for i, (vector, text) in enumerate(zip(vectors, texts)):
        doc_id = f"doc_{i}"
        collection.add(doc_id, {"text": text, "embedding": vector})
    return collection

def query_engine(query: str, collection: object) -> List[dict]:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vector = model.encode(query)
    results = collection.query(embedding=query_vector.tolist(), n_results=5, include=["embeddings", "documents", "metadatas"])
    return results
