# from langchain_ollama import ChatOllama
# from langchain.agents import initialize_agent, Tool, AgentType

# from tools.arithmetics import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
# from tools.algebra_tools import solve_algebra
# #Tools
# tools = [
#     Tool(
#         name="Addition Tool",
#         func=add_numbers,
#         description="Adds numbers separated by spaces or commas."
#     ),
#     Tool(
#         name="Subtraction Tool",
#         func=subtract_numbers,
#         description="Subtracts numbers."
#     ),
#     Tool(
#         name="Multiplication Tool",
#         func=multiply_numbers,
#         description="Multiplies numbers."
#     ),
#     Tool(
#         name="Division Tool",
#         func=divide_numbers,
#         description="Divides two numbers (a b)."
#     ),
#     Tool(
#         name="Algebra Solver",
#         func=solve_algebra,
#         description="Solves algebraic equations like '2x^2 + 3x - 5 = 0'."
#     ),
# ]
# #LLM
# llm = ChatOllama(
#     model="llama3.1:8b",
#     temperature=0,
#     streaming=False,     #disable streaming
#     num_ctx=4096
# )

# #Classic Agent
# math_agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # ✅ no tool-schema, works with Ollama
#     verbose=True,
#     handle_parsing_errors=True,
#     max_iterations= 5
# )


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
