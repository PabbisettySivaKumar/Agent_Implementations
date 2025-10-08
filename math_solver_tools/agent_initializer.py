from langchain_ollama import ChatOllama
from tools.arithmetics import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
from tools.algebra_tools import solve_algebra

#Initialize Ollama LLM
llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
    streaming=False
)

#Define tool registry
TOOLS = {
    "add": add_numbers,
    "sum": add_numbers,
    "plus": add_numbers,
    "subtract": subtract_numbers,
    "minus": subtract_numbers,
    "difference": subtract_numbers,
    "multiply": multiply_numbers,
    "times": multiply_numbers,
    "divide": divide_numbers,
    "quotient": divide_numbers,
    "algebra": solve_algebra,
    "solve": solve_algebra,
}
