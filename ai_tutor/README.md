# 🧠 AI Tutor  
### Built with LangChain · Ollama · ChromaDB · Neo4j · Streamlit  

A simple **AI Tutor** that learns from your uploaded PDFs, generates short quizzes using local AI (Ollama), and stores your score in Neo4j.  
Everything runs **locally** — no external APIs needed.

---

## 🚀 Features
- 📘 Upload PDF learning material  
- 🧩 Generate up to **10 quiz questions** using **Ollama (llama3)**  
- 🧮 Answer questions on the same page  
- 🎯 Get your score instantly  
- 💾 Save your score and user details in **Neo4j**  
- 🧠 Uses **Ollama nomic-embed-text** embeddings and **ChromaDB** for context retrieval  

---

## 🧩 Tech Stack

| Component | Tool |
|------------|------|
| **LLM** | Ollama (`llama3`) |
| **Embeddings** | Ollama (`nomic-embed-text`) |
| **Vector DB** | ChromaDB |
| **Graph DB** | Neo4j |
| **Framework** | LangChain |
| **UI** | Streamlit |

---

## 📁 Folder Structure

```
ai_tutor/
│
├── app.py         # Streamlit UI
│
├── agents/
│   ├── tutor_agent.py            # Ollama LLM
│   ├── knowledge_agent.py        # Search Chroma
│   └── quiz_generator.py         # Quiz creation
│
├── ingest/
│   ├── embeddings.py             # Ollama embeddings
│   └── pdfuploader.py            # PDF → Chroma pipeline
│
├── graph/
│   └── neo4j_setup.py            # Neo4j helper
│
├── progress/
│   └── user_score.py             # Store score in Neo4j
│
├── .env
│
└── requirements.txt
```

---

## ⚙️ Setup

### 1️⃣ Clone and install
```bash
git clone https://github.com/PabbisettySivaKumar/Agent_Implementations.git
cd ai_tutor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Configure `.env`
Create a file at `config/.env`:

```bash
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=yourpassword

CHROMA_PERSIST_DIR=./data/chroma_db
NOMIC_OLLAMA_MODEL=nomic-embed-text
```

---

## 🧰 Requirements
```
streamlit
langchain>=0.0.300
neo4j
chromadb
pdfplumber
python-dotenv
langchain_community
ollama
```

---

## 🦙 Start Ollama
```bash
ollama serve
ollama pull llama3
ollama pull nomic-embed-text
```

---

## 🕸️ Start Neo4j
```bash
neo4j start
```
Open Neo4j browser → [http://localhost:7474](http://localhost:7474)

---

## ▶️ Run Streamlit
```bash
streamlit run app.py
```

---

## 💻 How to Use

1. Enter your **name**.  
2. **Upload a PDF** (study material).  
3. Type a **topic or keyword** (e.g., “Photosynthesis”).  
4. Choose the number of questions (max 10).  
5. Click **“Generate Quiz”**.  
6. Answer the questions directly below.  
7. Click **“Submit”** to see your score.  
8. Your score is automatically saved to **Neo4j**.

---

## 🧮 Example Neo4j Graph

```
(User {name:"Siva"})
  └─[:TOOK]→(Attempt {score:8, total:10})
                   └─[:OF]→(Quiz {topic:"Photosynthesis"})
```

---

## 🔍 Example Neo4j Queries

**All user quiz attempts**
```cypher
MATCH (u:User)-[:TOOK]->(a:Attempt)-[:OF]->(q:Quiz)
RETURN u.name, q.topic, a.score, a.total, a.created_at
ORDER BY a.created_at DESC;
```

**Leaderboard**
```cypher
MATCH (u:User)-[:TOOK]->(a:Attempt)
RETURN u.name, round(avg(1.0*a.score/a.total*100),1) AS avg_percent
ORDER BY avg_percent DESC LIMIT 10;
```

---

## 🧱 Architecture Overview

```
        ┌──────────────┐
        │     PDF      │
        │   Upload     │
        └──────┬───────┘
               │ Extract & Chunk
               ▼
        ┌──────────────┐
        │   ChromaDB   │
        │  (Embeddings)│ ← nomic-embed-text (Ollama)
        └──────┬───────┘
               │ Semantic Search
               ▼
        ┌──────────────┐
        │   Ollama LLM │ ← llama3
        │   via LangChain
        └──────┬───────┘
               │ Generate Quiz (JSON)
               ▼
        ┌──────────────┐
        │   Neo4j DB   │
        │  (Users, Quiz, Attempts)
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │  Streamlit   │
        │     UI       │
        └──────────────┘
```

---

## 🧩 Example Run

1️⃣ Upload → `biology_chapter_5.pdf`  
2️⃣ Topic → `Photosynthesis`  
3️⃣ Generate 8 Questions  
4️⃣ Answer → Submit → **🎯 Your Score: 6/8**  
5️⃣ Check Neo4j → `(User)-[:TOOK]->(Attempt)-[:OF]->(Quiz)` ✅  

---

## 🧠 Future Enhancements
- Show correct answers after submission  
- Add leaderboard in Streamlit  
- Track user progress over time  
- Support multiple PDFs per topic  

---

## 🧾 License
MIT License © 2025 [@itsPSK95][https://x.com/itsPSK95]

---

## ⚡ Troubleshooting

| Problem | Fix |
|----------|-----|
| **Ollama model not found** | Run `ollama pull llama3` and `ollama pull nomic-embed-text` |
| **Neo4j auth error** | Update `.env` with correct username/password |
| **Chroma path error** | Create `./data/chroma_db` manually if missing |
| **Streamlit port conflict** | Run `streamlit run app.py --server.port 8502` |

---