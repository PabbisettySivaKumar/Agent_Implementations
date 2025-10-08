from langchain_ollama import OllamaLLM
from langchain.schema import HumanMessage

class OrchestratorAgent:
    def __init__(self, model_name="llama3.1:8b", temperature=0.3):
        self.llm = OllamaLLM(model=model_name, temperature=temperature)

    def summarize(self, innovation_eval, feasibility_eval, monetization_eval):
        prompt = f"""
        You are the final evaluator summarizing three expert reviews.

        INNOVATION:
        {innovation_eval}

        FEASIBILITY:
        {feasibility_eval}

        MONETIZATION:
        {monetization_eval}

        Combine them and provide:
        - Summary (max 100 words)
        - Final average score out of 10
        - Verdict: "Strong Idea", "Moderate Idea", or "Weak Idea"
        """
        return self.llm.invoke([HumanMessage(content=prompt)])
