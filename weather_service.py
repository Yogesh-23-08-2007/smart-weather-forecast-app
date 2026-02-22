import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")


def fetch_weather(city_name):

  url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

  response=requests.get(url)

  if response.status_code==200:
    data=response.json()
    return {
          "city": city_name,
          "temp": data["main"]["temp"],
          "humidity": data["main"]["humidity"],
          "wind_speed":data['wind']['speed'],
          "feels_like":data['main']['feels_like'],
          "description": data["weather"][0]["description"]
      }

  else:
    raise Exception("City not found or API error")