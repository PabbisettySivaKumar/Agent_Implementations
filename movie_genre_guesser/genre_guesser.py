from serper_client import fetch_movie_data
from llm_client import extract_genre_with_llm

def guess_movie_genre(mv_title: str):
    data= fetch_movie_data(mv_title)

    snippets= []
    if 'organic' in data:
        for result in data['organic']:
            snippet= result.get('snippet', '')
            if snippet:
                snippets.append(snippet)

    return extract_genre_with_llm(mv_title, snippets[:5])