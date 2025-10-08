import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY= os.getenv('SERPER_API_KEY')

def fetch_movie_data(mv_title: str):
    url= 'https://google.serper.dev/search'
    headers= {
        'X-API_KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    payload= {
        'q': f'{mv_title} movie genre', 
        "num": 5
    }
    response= requests.post(url, headers= headers, json= payload)
    if response.status_code !=200:
        return {'error': f'serper api error {response.status_code}: {response.text}'}
    data= response.json()
    result= data.get("organic", [])

    if results:
        snippets = [r.get("snippet", "") for r in results]
        return {"snippets": snippets}
    
    return {"message": "No movie data found."}