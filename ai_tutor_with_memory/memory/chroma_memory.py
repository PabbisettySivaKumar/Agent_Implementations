from langchain_community.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()

def get_chroma_memory():
    persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./chroma_persist")
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text:latest", 
        base_url=os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
    )
    vectorstore = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    return vectorstore, memory
