from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ollama
from tools.serper_tool import fetch_movie_data

app = FastAPI(title="Movie Genre Guesser (Agents Only)")

class MovieRequest(BaseModel):
    movie: str

@app.post("/predict-genre")
async def predict_genre(request: MovieRequest):
    try:
        movie_info = fetch_movie_data(request.movie)
        if isinstance(movie_info, dict):
            snippets = movie_info.get("snippets", [])
            text_context = "\n".join(snippets)
        else:
            text_context = str(movie_info)

        prompt = f"""
        You are a movie genre prediction expert.
        Below is information about a movie. Based on this info,
        predict the most likely genre(s).

        Movie: {request.movie}
        Information: {text_context}

        Return only the genre(s), comma-separated.
        """

        response = ollama.chat(
            model="llama3.1:8b", 
            messages=[{"role": "user", "content": prompt}]
            )
        answer = response["message"]["content"].strip()

        return {"predicted_genre": answer}

    except Exception as e:
        import traceback
        print("ERROR OCCURRED:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
