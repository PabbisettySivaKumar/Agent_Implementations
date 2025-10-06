from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

class IdeaAgent:
    def __init__(self):
        self.model= Ollama(
            model= os.getenv("OLLAMA_MODEL", "mistral:latest"),
            base_url= os.getenv("OLLAMA_URL")
        )

    def analyze_idea(self, idea:str) -> str:
        prompt= f"""
You are a startup idea analyst. Evaluate the following startup idea:

Idea: {idea}

Provide:
1. Summary of the idea
2. Innovation and uniqueness
3. Strengths and weaknesses
4. Possible improvements        
"""
        return self.model.invoke(prompt)