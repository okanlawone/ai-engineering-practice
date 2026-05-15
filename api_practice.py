import requests
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

def get_weather(city=None): 
    if city is None: 
        city = input("Enter city: ").strip()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

    response = requests.get(url)
    data =  response.json()

    if response.status_code != 200:
        print(f"Error: {data['message']}")
        return

    print(response.status_code)

    print(f"City: {data['name']}")
    print(f"Current Temp: {data['main']['temp']}F")
    print(f"Feels Like: {data['main']['feels_like']}F")
    print(f"Condition: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}")

get_weather("xyabz")