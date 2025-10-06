from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

class MarketAgent:
    def __init__(self):
        self.model= Ollama(
            model= os.getenv("OLLAMA_MODEL", "mistral:latest"),
            base_url= os.getenv("OLLAMA_URL")
        )

    def market_research(self, idea:str) -> str:
        prompt= f"""
You are a market research specialist. For the startup idea below, analyze:

Idea: {idea}

Provide:
1. Target audience and demographics
2. Market demand and trends
3. Competitor landscape
4. Market entry strategy        
"""
        return self.model.invoke(prompt)