# 💡 Startup Idea Evaluator (LangChain + Ollama)

An intelligent evaluator that analyzes startup ideas for **Innovation**, **Feasibility**, and **Monetization Potential** using **LangChain agents** and **Ollama** local models.

The app runs with a simple **Streamlit interface** and helps founders, investors, or students validate their ideas instantly — all locally, without any cloud dependencies.

## 🚀 Features

- Multi-agent architecture:
  - **InnovationAgent** → Analyzes originality and novelty.
  - **FeasibilityAgent** → Evaluates practicality and implementation.
  - **MonetizationAgent** → Checks business and profit potential.
  - **OrchestratorAgent** → Summarizes and rates the idea overall.
- Generates structured, easy-to-read evaluation reports.
- Works entirely offline using Ollama’s local models.
- Simple, user-friendly Streamlit interface.

## 🧩 Architecture

```
idea_evaluator/
│
├── agents/
│   ├── innovation_agent.py
│   ├── feasibility_agent.py
│   ├── monetization_agent.py
│
│── orchestrator_agent.py
├── main.py
├── .env
└── requirements.txt
```

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai) installed
- Model pulled locally:
  ```bash
  ollama pull llama3
  ```

### 2️⃣ Clone and Install
```bash
git clone https://github.com/yourusername/idea_evaluator.git
cd idea_evaluator
pip install -r requirements.txt
```

### 3️⃣ Create `.env`
```bash
MODEL_NAME=llama3
TEMPERATURE=0.3
```

## ▶️ Run the App

```bash
streamlit run main.py
```

Then open the app at 👉 [http://localhost:8501](http://localhost:8501)

## 🧠 Example Output

**Idea:** AI-based plant disease detection using camera input.

```
📘 Innovation
Score: 8/10
Reason: Novel application of AI in agriculture with real-world benefits.

📘 Feasibility
Score: 7/10
Reason: Requires dataset and model training but technically achievable.

📘 Monetization
Score: 9/10
Reason: Strong business model through subscription or per-scan pricing.

📘 Final Summary
Overall Score: 8/10
Verdict: Strong Idea
Comment: A well-rounded idea combining technology, social impact, and scalability.
```

## 🧰 Tech Stack

- 🧩 **LangChain**
- 🦙 **Ollama (Llama 3 model)**
- 🧠 **Python**
- 🖥️ **Streamlit**

## 💡 Future Enhancements

- Add market viability scoring.
- Integrate vector database for idea similarity search.
- Compare with top 100 startup trends.
- Export report as PDF.

## 👨‍💻 Author

**Siva Kumar**  
Built with ❤️ using LangChain + Ollama
