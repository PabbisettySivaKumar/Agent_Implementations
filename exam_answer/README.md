# 🧠 Exam Answer Revisor (LangChain + Ollama)

An AI-powered tool that evaluates and revises students’ written exam answers based on **Concept Accuracy**, **Clarity**, and **Completeness** — built using the **LangChain** framework and **Ollama** local LLMs.

The app runs locally with a simple **Streamlit UI**, providing feedback and improved rewritten answers instantly.

## 🚀 Features

- Evaluates answers using multiple specialized agents:
  - **ConceptClarityAgent** → Checks factual correctness and writing clarity.
  - **CompletenessAgent** → Ensures coverage of all key points.
  - **RevisorAgent** → Summarizes and generates an improved version.
- Provides **structured feedback** with individual scores and comments.
- Fully **on-device** with Ollama — no external API calls.
- Streamlit interface for easy interaction.
- Modular design using LangChain Agents.

## 🧩 Architecture

```
exam_revisor/
│
├── agents/
│   ├── concept_clarity.py
│   ├── completeness.py
│   └── revisor.py
│
├── main.py
├── .env
└── requirements.txt
```

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai) installed locally
- `llama3` or compatible model pulled:  
  ```bash
  ollama pull llama3
  ```

### 2️⃣ Clone and Install
```bash
git clone https://github.com/PabbisettySivaKumar/Agent_Implementations.git
cd exam_revisor
pip install -r requirements.txt
```

### 3️⃣ Create `.env`
```bash
MODEL_NAME=llama3.1:8b
TEMPERATURE=0.3
```

## ▶️ Run the App

```bash
streamlit run main.py
```

Then open the app at 👉 [http://localhost:8501](http://localhost:8501)

## 🧠 Example Output

**Question:** What is machine learning?  
**Answer:** Machine learning is when computers learn by themselves.

```
📘 Concept & Clarity
Concept Accuracy:
Score: 4/10
Reason:
The answer is partially correct but lacks explanation of how machines learn from data.

Clarity & Structure:
Score: 5/10
Reason:
The answer is clear but too simplistic.

Overall Comment:
The student demonstrates basic understanding but needs to define the process more accurately.

📘 Completeness
Score: 3/10
Reason:
The definition omits key points like algorithms, data, and model training.
```

## 🧰 Tech Stack

- 🧩 **LangChain**
- 🦙 **Ollama (Llama 3 model)**
- 🧠 **Python**
- 🖥️ **Streamlit**

## 💡 Future Enhancements

- Add grammar and tone agent.
- Allow answer comparison with an answer key.
- Support bulk student evaluation.
- Export reports as PDF.

## 👨‍💻 Author

**Siva Kumar** [@itsPSK95][https://x.com/itsPSK95]  
Built with ❤️ using LangChain + Ollama
