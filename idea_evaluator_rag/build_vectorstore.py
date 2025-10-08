from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from utils.config import CHROMA_DB_DIR
from tqdm import tqdm

def build_vectorstore():
    print("Building Chroma vectorstore...")
    embedding_fn = OllamaEmbeddings(model="nomic-embed-text", base_url="http://127.0.0.1:11434")

    with open("data/startup_examples.txt", "r") as f:
        ideas = [line.strip() for line in f if line.strip()]

    Chroma.from_texts(ideas, embedding_fn, persist_directory=CHROMA_DB_DIR)
    print(f"Stored {len(ideas)} startup ideas in {CHROMA_DB_DIR}")

if __name__ == "__main__":
    build_vectorstore()
