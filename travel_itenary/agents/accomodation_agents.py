from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.config import OLLAMA_MODEL, OLLAMA_URL

def accommodation_agent(llm):
    llm = Ollama(
        model=OLLAMA_MODEL, 
        base_url=OLLAMA_URL
        )
    prompt = PromptTemplate.from_template("""
You are an accommodation advisor.

Input:
Destination: {destination}
Budget: {budget}
Duration: {duration} days

Provide:
1. Recommended hotels, hostels, or Airbnbs
2. Average nightly cost
3. Why they fit the user’s preferences
    """)
    return prompt | llm
