from langchain import PromptTemplate

TUTOR_TEMPLATE = """
You are a friendly and patient AI tutor.

Past conversation memory:
{chat_history}

Student question:
{question}

Provide:
1. A concise answer
2. Step-by-step reasoning
3. A short exercise for practice
"""

tutor_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=TUTOR_TEMPLATE,
)
