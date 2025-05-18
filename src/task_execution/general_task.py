import google.generativeai as genai
from utils.config import GOOGLE_API_KEY
import re

genai.configure(api_key=GOOGLE_API_KEY)

def clean_response(text):
    # Remove markdown formatting
    text = re.sub(r'\*\*', '', text)  # Remove bold formatting
    text = re.sub(r'\*', '', text)    # Remove italic formatting
    text = re.sub(r'#', '', text)     # Remove heading formatting
    
    # Remove bullet points
    text = re.sub(r'^\s*[\-\*]\s', '', text, flags=re.MULTILINE)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def get_general_response(query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    
    # Clean the response
    cleaned_response = clean_response(response.text)
    
    return cleaned_response