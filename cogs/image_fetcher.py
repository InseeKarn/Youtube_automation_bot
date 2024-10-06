import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def fetch_image(query):
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    url = f'https://api.unsplash.com/photos/random?query={query}&client_id={access_key}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        if 'results' in data and data['results']:
            return data['results'][0]['urls']['regular']
        else:
            return None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None