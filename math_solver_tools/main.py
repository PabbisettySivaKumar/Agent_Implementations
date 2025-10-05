from fastapi import FastAPI
from pydantic import BaseModel
from agent_initializer import llm, TOOLS  # import tool registry + LLM
import time

app = FastAPI(title="Math Solver (Hybrid Agent)", description="Fast local math solver using Llama3.1 + custom tools")

class MathPrompt(BaseModel):
    question: str

@app.post("/solve")
async def solve_math(query: MathPrompt):
    start = time.time()
    q = query.question.lower()

    try:
        #run tool
        for keyword, func in TOOLS.items():
            if keyword in q:
                result = func(q)
                duration = round(time.time() - start, 2)
                return {
                    "Prompt": query.question,
                    "Tool Used": func.__name__,
                    "Answer": result.get("output", result),
                    "Time (s)": duration
                }

        #LLM reasoning
        response = llm.invoke(f"Solve step-by-step: {query.question}")
        duration = round(time.time() - start, 2)
        return {
            "Prompt": query.question,
            "Tool Used": "LLM (WizardMath/Llama3)",
            "Answer": response.content,
            "Time (s)": duration
        }

    except Exception as e:
        return {"error": str(e)}
