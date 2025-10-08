from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.config import OLLAMA_MODEL, OLLAMA_URL

def budget_agent(llm):
    llm = Ollama(
        model=OLLAMA_MODEL, 
        base_url=OLLAMA_URL
        )
    prompt = PromptTemplate.from_template("""
You are a travel budgeting expert.

Input:
Destination: {destination}
Duration: {duration} days
Base budget: {budget}

Output:
1. Estimated total cost (accommodation + travel + food + activities)
2. Budget breakdown
3. Tips to save money or optimize the trip
    """)
    return prompt | llm