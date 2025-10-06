from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

def get_ollama_model():
    model_name = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
    base_url = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
    llm = Ollama(model=model_name, base_url=base_url)
    return llm
