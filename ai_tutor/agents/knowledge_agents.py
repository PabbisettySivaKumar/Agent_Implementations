import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from doc_uploader.embeddings import NomicOllamaEmbeddings

load_dotenv()
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma_db")

def semantic_search_resource(query: str, top_k: int = 5):
    """Simple search for relevant text chunks from Chroma."""
    embeddings = NomicOllamaEmbeddings()
    store = Chroma(persist_directory=CHROMA_PERSIST_DIR, embedding_function=embeddings)
    docs = store.similarity_search_with_score(query, k=top_k)
    return "\n".join([d.page_content for d, _ in docs])
