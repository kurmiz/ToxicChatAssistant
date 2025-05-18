# Web search task module 
import requests
from utils.config import GOOGLE_SEARCH_API_KEY

def web_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': GOOGLE_SEARCH_API_KEY,
        'cx': '017576662512468239146:omuauf_lfve',  # Replace with your actual search engine ID
        'q': query
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            return f"Here's what I found: {data['items'][0]['snippet']}"
        else:
            return "Sorry, I couldn't find any relevant information."
    else:
        return "Sorry, I couldn't perform the web search."
