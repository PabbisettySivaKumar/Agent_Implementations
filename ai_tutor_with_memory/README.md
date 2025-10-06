# AI Tutor with Memory
A Local **LangChain + Ollama + Chroma-based Intelligent Tutor**
---
## Overview

AI Tutor with Memory is an intelligent, privacy-preserving tutoring assistant built entirely with **LangChain**, **Ollama**, and **ChromaDB**.

It can:

-Remember previous questions and answers (context-aware tutoring)

-Retrieve past discussions using vector embeddings

-Generate explanations, examples, and practice questions

-Run fully offline — all models are local (no cloud dependency)

The app uses:

-mistral:latest (or any Ollama model of your choice) for reasoning

-nomic-embed-text:latest for generating embeddings

-Chroma for persistent local memory

-Streamlit for a fast and simple user interface

---
## Project Structure

```bash
ai_tutor_with_memory/
├── app.py                         # Streamlit main app
├── chains/
│   ├── __init__.py
│   └── tutor_chains.py            # LangChain conversational chain
├── llms/
│   ├── __init__.py
│   └── ollama_llm.py              # Ollama model setup
├── memory/
│   ├── __init__.py
│   └── chroma_memory.py           # Embeddings + vectorstore config
├── prompts/
│   ├── __init__.py
│   └── tutor_prompt.py            # Prompt template for tutor behavior
├── utils/
│   ├── __init__.py
│   └── config.py                  # Optional .env variable loader
├── .env                           # Environment variables
└── requirements.txt               # Dependencies
```
---
## Installation

### 1. Clone & enter the project
```bash
git clone https://github.com/yourusername/ai_tutor_with_memory.git
cd ai_tutor_with_memory
```
### 2. Create & activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
OR
 .\venv\Scripts\activate          # Windows PowerShell
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
---
## Install Ollama and Models
1. Install Ollama → https://ollama.com/download
2. Start Ollama:
```bash
ollama serve
```
3. Pull the models:
```bash
ollama pull mistral:latest
ollama pull nomic-embed-text:latest
```
---
## Setup Environment Variables
Create a file named .env in your project root and add:
```bash
OLLAMA_URL=http://127.0.0.1:11434
OLLAMA_MODEL=mistral:latest
CHROMA_PERSIST_DIR=./chroma_persist
TUTOR_DEFAULT_USER=student_1
```
---
## Running the App
Once Ollama is running:
```bash
streamlit run app.py
```
Open the local URL (usually http://localhost:8501/) in your browser.
---
## Using the Tutor
1. Type your question (math, coding, general knowledge, etc.)
2. Press Ask — the tutor will:

    -Retrieve relevant context from your saved memory
    -Generate a step-by-step answer
    -Suggest a small practice question

3. Each Q/A pair is stored in Chroma for future sessions.
Memory persists even after you close the app!
---
## Example Questions
-“Explain the Pythagorean theorem with an example.”

-“Differentiate x² + 3x + 2.”

-“What’s a binary search algorithm?”

-“Give me an exercise to practice derivatives.”
---
## Clearing Memory
To reset or start fresh:
```bash
rm -rf ./chroma_persist
```


