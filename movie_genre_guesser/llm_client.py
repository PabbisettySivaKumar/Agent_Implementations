import subprocess
import json
import ast

GENRE_LIST= [
    "Action", "Comedy", "Romance", "Drama", "Sci-Fi", "Horror", "Thriller",
    "Animation", "Fantasy", "Mystery", "Crime", "Adventure", "Family",
    "Documentary", "War", "Western", "Musical"
]

def extract_genre_with_llm(mv_title: str, snippets: list, model: str= 'mistral'):
    '''Send snippets to Ollama for Structured Genre extraction'''
    context= '\n'.join(snippets)
    prompt= f"""
    
You are a movie genre classifer.
valid genres: {', '.join(GENRE_LIST)}

Movie: {mv_title}
snippets: {context}
    
Extract the most relevant 2-3 genres from the snippets.
Return only JSON in this format:
{{'genres: ['Genre1', 'Genre2']}}
"""

    result= subprocess.run(
        ['ollama', 'run', model],
        input= prompt.encode(),
        capture_output= True
    )
    raw_output= result.stdout.decode().strip()
    print('Ollama Output:', raw_output)
    try:
        if raw_output.startswith("```"):
            raw_output = raw_output.strip("`").replace("json", "").strip()

        parsed = json.loads(raw_output)
        if isinstance(parsed, dict) and "genres" in parsed:
            return parsed

    except Exception:
        try:
            parsed = ast.literal_eval(raw_output)
            if isinstance(parsed, dict) and "genres" in parsed:
                return parsed
        except Exception as e:
            print("Parsing failed:", e, "\nRaw output:", raw_output)

    return {"genres": ["Unknown"]}