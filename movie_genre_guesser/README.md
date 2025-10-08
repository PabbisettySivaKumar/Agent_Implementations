Movie Genre Guesser

An AI-powered API that predicts a movie’s genres using:

Serper API → fetches movie info from Google search results

Ollama LLM → extracts and normalizes genres

FastAPI → serves results via REST API

Features

Guess movie genres from a title (or description)
Uses real-time search results (via Serper)
Leverages local LLM (Ollama) for genre extraction
Always returns clean JSON output
Modular code (separate files for Serper, LLM, core logic, API)

Project Structure

 ```bash

movie_genre_guesser/
│── main.py            # FastAPI entrypoint
│── serper_client.py   # Handles Serper API calls
│── llm_client.py      # Handles Ollama LLM calls (JSON parsing)
│── genre_guesser.py   # Core logic (Serper + LLM)
│── requirements.txt   # Dependencies
│── .env               # API key (not committed to GitHub)
```

Requirements

Python 3.9+

Ollama installed locally
Serper API key

Setup

Clone repo
```bash
git clone https://github.com/PabbisettySivaKumar/Agent_Implementations.git
cd movie_genre_guesser
```
Create venv & install deps
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```
Set environment variables
Create a .env file:
```bash
SERPER_API_KEY=your_serper_api_key_here
```
Run API
```bash
uvicorn main:app --reload
```

Usage

Open in browser or use curl:
```nginx
GET http://127.0.0.1:8000/guess_genre?movie=Inception
```
Example Response:
```json
{
  "movie": "Inception",
  "genres": ["Action", "Sci-Fi", "Thriller"]
}
```
Example Movies
```bash
/guess_genre?movie=Bahubali
/guess_genre?movie=Tenet
/guess_genre?movie=Batman
```

Tech Stack

FastAPI – API framework

Serper API – Google Search API

Ollama (Mistral/Llama2) – Local LLM

Python AST/JSON – Robust parsing
