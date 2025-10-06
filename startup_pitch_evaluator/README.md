## Startup Pitch Team (Multi-Agent System)

### ***A LangChain + Ollama powered multi-agent system that simulates a startup founding team — analyzing your startup idea from multiple expert perspectives and automatically generating a investor pitch deck.***
---
### Overview

The Startup Pitch Team acts as your personal startup analysis board:

- Idea Analyst Agent – Evaluates originality and feasibility

- Market Research Agent – Studies demand, competitors, and user segments

- Financial Analyst Agent – Estimates costs, revenue, and ROI

- Pitch Writer Agent – Creates a polished investor pitch

- Orchestrator – Coordinates all agents and compiles the results

Finally, the system automatically generates a PowerPoint pitch deck using the insights from all agents.

Everything runs locally using Ollama — no cloud dependencies or API keys required.

---

### Features
Feature	Description
- Multi-Agent Collaboration	Each agent specializes in one startup domain
- Built with LangChain	Uses LLMChains for modular orchestration
- Streamlit UI	Simple and interactive front-end
- Fully Local	Works with local Ollama models — private & offline

---

### Project Structure

```bash
startup_pitch_team/
├── app.py                         # Streamlit main app
├── orchestrator.py                 # Coordinates agents and creates PPT
├── agents/
│   ├── __init__.py
│   ├── idea_agent.py               # Idea evaluation agent
│   ├── market_agent.py             # Market research agent
│   ├── finance_agent.py            # Financial analysis agent
│   └── pitch_agent.py              # Pitch writing agent
├── utils/
│   ├── __init__.py
│   ├── config.py                   # Loads .env variables
├── requirements.txt
└── .env
```
---
### Installation
1. Clone & enter the project
```bash
git clone https://github.com/PabbisettySivaKumar/Agent_Implementations.git
cd startup_pitch_team
```
2. Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
 .\venv\Scripts\activate         # Windows
```
3. Install dependencies

```bash
pip install -r requirements.txt
```
---
### Install Ollama and Models
1. Install Ollama → https://ollama.com/download
2. Start Ollama:
```bash
ollama serve
```
3. Pull the models:
```bash
ollama pull llama3.1:latest
```
---
### Setup Environment Variables
Create a file named .env in your project root and add:
```bash
OLLAMA_URL=http://127.0.0.1:11434
OLLAMA_MODEL=mistral:latest
CHROMA_PERSIST_DIR=./chroma_persist
TUTOR_DEFAULT_USER=student_1
```
---
### Running the App
Once Ollama is running:
```bash
streamlit run app.py
```
Open the local URL (usually http://localhost:8501/) in your browser.

---
### Using the App

Enter your startup idea (e.g. “AI-powered plant health detection app for farmers.”)

Click “Generate Pitch”

Wait while all agents collaborate

View:

- Idea Summary

- Market Research

- Financial Analysis

- Final Pitch Narrative

---
### Example Output

```pgsql
✅ Idea analysis complete.
✅ Market research complete.
✅ Financials done.
✅ Pitch generated.
```
