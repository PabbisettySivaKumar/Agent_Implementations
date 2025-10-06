from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

class PitchAgent:
    def __init__(self):
        self.model= Ollama(
            model= os.getenv("OLLAMA_MODEL", "mistral:latest"),
            base_url= os.getenv("OLLAMA_URL")
        )

    def write_pitch(self, idea_summary:str, market: str, financials: str) -> str:
        prompt= f"""
You are a startup pitch writer. Combine the following insights to draft a startup pitch deck summary.

Idea Summary:
{idea_summary}

Market Analysis:
{market}

Financials:
{financials}

Provide:
1. Compelling pitch narrative (1 paragraph)
2. Elevator pitch (2 sentences)
3. Suggested pitch deck slide titles (5–7 slides)        
"""
        return self.model.invoke(prompt)