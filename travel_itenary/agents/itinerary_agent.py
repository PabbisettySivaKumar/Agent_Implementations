from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.config import OLLAMA_MODEL, OLLAMA_URL

def itinerary_agent(llm):
    llm = Ollama(
        model=OLLAMA_MODEL, 
        base_url=OLLAMA_URL
        )
    prompt = PromptTemplate.from_template("""
You are a travel itinerary coordinator.

Combine all the details below into a final daily itinerary.

Destination Suggestions:
{destinations}

Accommodation:
{accommodation}

Activities:
{activities}

Budget Details:
{budget}

Output:
- 3–5 day structured itinerary with morning/afternoon/evening plans.
- Include total estimated cost.
- End with a short summary of the trip theme (e.g., adventure, relaxation, culture).
    """)
    return prompt | llm