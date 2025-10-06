from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

class FinancialAgent:
    def __init__(self):
        self.model= Ollama(
            model= os.getenv("OLLAMA_MODEL", "mistral:latest"),
            base_url= os.getenv("OLLAMA_URL")
        )

    def analyze_financials(self, idea:str) -> str:
        prompt= f"""
You are a financial analyst. For the startup idea below, estimate:

Idea: {idea}

Provide:
1. Cost structure and key expenses
2. Revenue model
3. Pricing strategy
4. 12-month financial projection (rough)
5. Break-even analysis        
"""
        return self.model.invoke(prompt)