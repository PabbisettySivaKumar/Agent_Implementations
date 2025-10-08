import streamlit as st
from dotenv import load_dotenv
import os

from agents.innovation_agent import InnovationAgent
from agents.feasibility_agent import FeasibilityAgent
from agents.monetization_agent import MonetizationAgent
from orchestrator_agent import OrchestratorAgent

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "llama3")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.3"))

def evaluate_idea(idea: str):
    innovation = InnovationAgent(MODEL_NAME, TEMPERATURE).evaluate(idea)
    feasibility = FeasibilityAgent(MODEL_NAME, TEMPERATURE).evaluate(idea)
    monetization = MonetizationAgent(MODEL_NAME, TEMPERATURE).evaluate(idea)

    orchestrator = OrchestratorAgent(MODEL_NAME, TEMPERATURE)
    summary = orchestrator.summarize(innovation, feasibility, monetization)

    results = {
        "Innovation": innovation,
        "Feasibility": feasibility,
        "Monetization": monetization,
        "Final Summary": summary
    }
    return results

st.set_page_config(page_title="Idea Evaluator", layout="centered")
st.title("AI-Powered Idea Evaluator")
st.markdown("Evaluate your startup or project idea using AI agents for innovation, feasibility, and monetization.")

idea = st.text_area("Enter your startup idea:", placeholder="e.g., AI-based plant health detection using camera input")

if st.button("Evaluate Idea"):
    if idea.strip():
        with st.spinner("Evaluating your idea..."):
            results = evaluate_idea(idea)
        st.success("Evaluation Complete!")

        for key, value in results.items():
            st.subheader(f"{key}")
            st.write(value)
    else:
        st.warning("Please enter an idea before evaluating.")

st.markdown("---")
st.caption("Built with LangChain Agents + Ollama LLMs")
