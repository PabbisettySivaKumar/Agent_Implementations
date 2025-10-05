# Math Solver Tools

A **local AI-powered math solver** built using **FastAPI**, **Ollama (Llama3.1:8B)**, and **custom Python tools** for arithmetic and algebraic operations.  
The system intelligently decides whether to use a local Python math tool or the LLM for advanced reasoning (like calculus or symbolic math).

---

## Features

- **Custom Math Tools** for:
  - Addition, Subtraction, Multiplication, Division
  - Algebraic Equation Solving
- **Hybrid Local Agent**:
  - Uses **Python tools** for basic math
  - Falls back to **Ollama (Llama3.1)** for complex problems
- **Fully Offline** — No cloud dependencies
- **FastAPI REST API** for local or production deployment
- 100% Private — Runs entirely on your device

---

## Project Structure

```bash
math_solver_tools
├── main.py
│   └─ FastAPI entry point — handles incoming requests and routes them to tools or LLM.
│
├── agent_initializer.py
│   └─ Initializes Ollama (Llama3.1) model and registers all available math tools.
│
├── tools/
│   ├── arithmetics.py
│   │   └─ Handles basic operations: addition, subtraction, multiplication, and division.
│   │
│   ├── algebra_tools.py
│   │   └─ Solves algebraic and polynomial equations using custom logic.
│   │
│   └── (optional future modules)
│       ├── calculus_tools.py → for derivatives & integration
│       ├── geometry_tools.py → for area, volume, and geometry operations
│
├── ollama_utils.py
│   └─ Helper utilities for interacting with Ollama or preprocessing model prompts.
│
└── README.md
    └─ Project overview, setup instructions, and API usage examples.
```
## Installation
1. Clone the Repository
```bash
git clone https://github.com/yourusername/math_solver_tools.git
cd math_solver_tools
```

2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)
````

3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Run the API

Start the FastAPI server:
```bash
uvicorn main:app --reload
```
