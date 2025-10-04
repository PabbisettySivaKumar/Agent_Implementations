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

    payload= {'q': f'{mv_title} movie genre'}
    response= requests.post(url, headers= headers, json= payload)
    return response.json()