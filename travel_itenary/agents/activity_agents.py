from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.config import OLLAMA_MODEL, OLLAMA_URL

def activity_agent(llm):
    llm = Ollama(
        model=OLLAMA_MODEL, 
        base_url=OLLAMA_URL
        )
    prompt = PromptTemplate.from_template("""
You are an activity planner.

Input:
Destination: {destination}
Interests: {interests}
Duration: {duration} days

Output:
1. Day-wise list of recommended activities
2. Local attractions or experiences
3. Tips or seasonal notes
    """)
    return prompt | llm
