import streamlit as st
import time
from langchain_ollama import OllamaLLM
from utils.config import OLLAMA_MODEL, OLLAMA_URL
from agents.destination_agents import destination_agent
from agents.accomodation_agents import accommodation_agent
from agents.activity_agents import activity_agent
from agents.budget_agents import budget_agent
from agents.itinerary_agent import itinerary_agent

def stream_section(title, chain, inputs):
    """Helper function to stream LLM output live into Streamlit."""
    st.subheader(title)
    placeholder = st.empty()
    output = ""

    for chunk in chain.stream(inputs):
        output += chunk
        placeholder.markdown(output)

    time.sleep(0.5)  
    return output


def build_itinerary(destination, duration, interests, budget):
    st.info("Building your travel itinerary with multiple AI agents...")

    llm = OllamaLLM(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_URL,
        options={"temperature": 0.6},
        streaming=True
    )

    dest_chain = destination_agent(llm)
    acc_chain = accommodation_agent(llm)
    act_chain = activity_agent(llm)
    bud_chain = budget_agent(llm)
    itin_chain = itinerary_agent(llm)

    destination_output = stream_section(
        "Destination Recommendations",
        dest_chain,
        {"destination": destination, "duration": duration, "interests": interests}
    )

    accommodation_output = stream_section(
        "Accommodation Suggestions",
        acc_chain,
        {"destination": destination, "budget": budget, "duration": duration}
    )

    activity_output = stream_section(
        "Activities Plan",
        act_chain,
        {"destination": destination, "interests": interests, "duration": duration}
    )

    budget_output = stream_section(
        "Budget Overview",
        bud_chain,
        {"destination": destination, "duration": duration, "budget": budget}
    )

    final_itinerary = stream_section(
        "Final Travel Itinerary",
        itin_chain,
        {
            "destinations": destination_output,
            "accommodation": accommodation_output,
            "activities": activity_output,
            "budget": budget_output
        }
    )

    st.success("Itinerary generation complete!")

    return {
        "destinations": destination_output,
        "accommodation": accommodation_output,
        "activities": activity_output,
        "budget": budget_output,
        "final_itinerary": final_itinerary
    }