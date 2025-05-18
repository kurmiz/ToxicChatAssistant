import requests
from utils.config import WEATHER_API_KEY

def get_weather(query):
    # Extract city name from query (this is a simplistic approach)
    city = query.split('weather in ')[-1] if 'weather in' in query else 'kathmandu'  # Default to London if no city specified
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The weather in {city} is {description} with a temperature of {temp}°C."
    else:
        return f"Sorry, I couldn't fetch the weather information for {city}. Please check if the city name is correct."