# 🧳 Travel Itinerary Planner (LangChain Agents)

This project is an AI-powered **Travel Itinerary Planner** built using **LangChain Agents**.  
It generates customized travel plans including destinations, accommodations, activities, and budget breakdowns.

---

## 🚀 Overview

The system uses multiple **specialized AI agents** orchestrated by a central **controller agent**.  
Each agent performs a specific role — from finding destinations to generating itineraries — and all are coordinated by the `orchestrator.py` module.

The frontend (`app.py`) exposes the functionality through a **Streamlit** or **FastAPI** interface.

---

## 🧩 Project Structure

```
travel_itenary/
│
├── agents/                  # Folder containing all LangChain agents
│   ├── accomodation_agents.py
│   ├── activity_agents.py
│   ├── budget_agents.py
│   ├── destination_agents.py
│   ├── itinerary_agent.py
│
├── utils/                   # Helper and utility scripts
│
├── venv/                    # Virtual environment (ignored by git)
│
├── .env                     # Environment variables (API keys, etc.)
├── .gitignore               # Git ignore rules
├── app.py                   # Entry point (Streamlit or FastAPI UI)
├── orchestrator.py          # Combines all agent outputs into final itinerary
├── requirements.txt         # Project dependencies
└── README.md                # Documentation file
```

---

## 🧠 How It Works

1. **User Input**: Enter a destination or country.
2. **Destination Agent**: Suggests popular cities or landmarks.
3. **Accommodation Agent**: Fetches hotel options and price ranges.
4. **Activity Agent**: Recommends things to do and experiences.
5. **Budget Agent**: Estimates total trip cost based on user preferences.
6. **Itinerary Agent**: Creates a structured multi-day itinerary.
7. **Orchestrator**: Aggregates all agent results and returns a complete travel plan.

---

## ⚙️ Setup & Installation

```bash
# Clone the repository
git https://github.com/yourusername/idea_evaluator.git
cd travel-itinerary-agents

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🧾 Environment Variables

Create a `.env` file in the root directory and include:

```bash
OLLAMA_URL=http://127.0.0.1:11434
OLLAMA_MODEL=mistral:latest
```

---

## ▶️ Run the App

### For **Streamlit**:
```bash
streamlit run app.py
```

---

## 📦 Example Output

```
Destination: Paris, France
Budget Range: ₹85,000 – ₹1,20,000
Recommended Hotels: Novotel, Ibis Styles
Top Activities: Eiffel Tower, Louvre Museum, Seine River Cruise

Day 1 - Arrival & Local Tour
Day 2 - Museum Visits & River Cruise
Day 3 - Shopping & Departure
```

---

## 🧰 Tech Stack

- **Python 3.10+**
- **LangChain Agents**
- **Streamlit**
- **Ollama Models / OpenAI**
- **dotenv** for managing API keys

---

## 🧑‍💻 Author

**Siva Kumar** [@itsPSK95][https://x.com/itsPSK95]  
Built with ❤️ using LangChain + Ollama

---

## 📝 License

This project is licensed under the **MIT License**.
