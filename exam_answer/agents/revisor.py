from langchain_ollama import OllamaLLM
#from langchain.schema import HumanMessage
import os

class RevisorAgent:
    def __init__(self, model_name= "llama3.1:8b", temperature= 0.3):
        self.llm= OllamaLLM(model= model_name, temperature= temperature)

    def summarize(self, question, answer, concept_clarity_eval, completeness_eval):
        prompt= f"""
        You are an exam evaluator summarizing the student's performance.

        Question: {question}
        Student's Original Answer: {answer}

        CONCEPT CLARITY EVALUATION:
        {concept_clarity_eval}

        COMPLETENESS EVALUATION:
        {completeness_eval}

        Combine the feedback and provide:
        - Summary feedback (max 100 words)
        - Final average score out of 10
        - Revised Answer (improved version)
        - Verdict: "Excellent", "Good", "Needs Improvement"
        """
        return self.llm.invoke(prompt)