from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

model = SentenceTransformer("all-MiniLM-L6-v2")

class SimpleChromaDB:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(name="doc_chunks")

    def add(self, chunks):
        embeddings = model.encode(chunks).tolist()
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        self.collection.add(documents=chunks, embeddings=embeddings, ids=ids)

    def query(self, query_text, top_k=5):
        query_embedding = model.encode([query_text]).tolist()[0]
        results = self.collection.query(query_embeddings=[query_embedding], n_results=top_k)
        return results["documents"][0]

def get_vector_store(chunks):
    db = SimpleChromaDB()
    db.add(chunks)
    return db
