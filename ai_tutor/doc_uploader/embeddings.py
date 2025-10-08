from langchain.embeddings.base import Embeddings
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

class NomicOllamaEmbeddings(Embeddings):
    def __init__(self, model_name=None):
        self.model_name = model_name or os.getenv("NOMIC_OLLAMA_MODEL", "nomic-embed-text")

    def embed_documents(self, texts):
        vectors = []
        for text in texts:
            resp = ollama.embeddings(model=self.model_name, prompt=text)
            vectors.append(resp["embedding"])
        return vectors

    def embed_query(self, text):
        resp = ollama.embeddings(model=self.model_name, prompt=text)
        return resp["embedding"]