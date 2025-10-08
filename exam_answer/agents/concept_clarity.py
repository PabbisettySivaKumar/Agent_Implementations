from langchain_ollama import OllamaLLM
#from langchain.schema import HumanMessage
import os

class concept_clarityAgent:
    def __init__(self, model_name= "llama3.1:8b", temperature= 0.3):
        self.llm= OllamaLLM(model= model_name, temperature= temperature)

    def evaluate(self, question: str, answer: str):
        prompt= f"""
        You are an expert exam evaluator. Evaluate the following student answer for the both ACCURACY and CLARITY.

        ---
        Question:
        {question}

        Answer:
        {answer}
        ---

        Perform the evaluation in two parts:
        1. **Concept Accuracy (0-10):**
           - Check if the key ideas are scientifically correct.
           - Identify if the explanation directly answer the question.
           - Penalize missing essential concept or incorrect reasoning.

        2. **Clarity & Structure (0-10):**
           - Check grammar, flow and logical organization.
           - Evaluate how clearly the answer communicate ideas.
           - Consider if it's well-strucutred, concise, and easy to follow.

        Provide your response in the **strict format below**:

        Concept Accuracy:\\n
        Score: <X>/10\\n
        Reason:
        <short explanation>

        Clarity & Structure:\\n
        Score: <X>/10\\n
        Reason: 
        <short explanation>

        Overall Comment:\\n
        <Provide a short paragraph combining both evaluations (max 60 words)>

        Make sure every 'Score' and 'Reason' label is followed by a newline (\\n).
        Do **not** place Score and Reason on the same line under any circumstance.
        """

        return self.llm.invoke(prompt)