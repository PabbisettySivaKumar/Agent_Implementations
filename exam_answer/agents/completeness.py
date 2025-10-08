from langchain_ollama import OllamaLLM
#from langchain.schema import HumanMessage
import os

class CompletenessAgent:
    def __init__(self, model_name= "llama3.1:8b", temperature= 0.3):
        self.llm= OllamaLLM(model= model_name, temperature= temperature)

    def evaluate(self, question: str, answer: str):
        prompt= f"""
        Evaluate the COMPLETENESS of the student's answer below.
        Question: {question}
        Answer: {answer}

        Check whether all key points of the topic are covered.
        Format strictly as:\\n
        Score: <X>/10\\n
        Reason: \\n
        <text>
        Make sure every 'Score' and 'Reason' label is followed by a newline (\\n).
        Do **not** place Score and Reason on the same line under any circumstance.
        """
        return self.llm.invoke(prompt)