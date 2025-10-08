from langchain_ollama import OllamaLLM
from langchain.schema import HumanMessage

class MonetizationAgent:
    def __init__(self, model_name="llama3.1:8b", temperature=0.3):
        self.llm = OllamaLLM(model=model_name, temperature=temperature)

    def evaluate(self, idea: str):
        prompt = f"""
        Evaluate the MONETIZATION potential of this idea: "{idea}".
        Consider scalability, profit models, and market demand.
        Give a score (0–10) and reasoning.
        Format:
        Score: X/10
        Reason: <text>
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response
