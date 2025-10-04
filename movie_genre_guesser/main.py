from fastapi import FastAPI, Query
from genre_guesser import guess_movie_genre

app= FastAPI(title= 'Movie Genre Guesser API')

@app.get('/guess_genre')
def guess_genre(movie: str= Query(..., description= 'Movie title')):
    genres= guess_movie_genre(movie)
    return {'movie': movie, 'genres': genres['genres']}