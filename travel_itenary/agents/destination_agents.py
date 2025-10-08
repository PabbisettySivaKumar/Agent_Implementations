from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.config import OLLAMA_MODEL, OLLAMA_URL

def destination_agent(llm):
    llm = Ollama(
    model=OLLAMA_MODEL, 
    base_url=OLLAMA_URL
    )
    prompt = PromptTemplate.from_template("""
You are a travel expert. Suggest top travel destinations and transport options based on:

User Input:
- Preferred destination or region: {destination}
- Duration: {duration} days
- Interests: {interests}

Output:
1. Recommended destinations or nearby attractions
2. Best transport options to reach there
3. Short summary of why it’s ideal
    """)
    return prompt | llm
