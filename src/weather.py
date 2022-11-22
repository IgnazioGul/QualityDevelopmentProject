import requests
from dotenv import load_dotenv
import os
load_dotenv()

OPEN_WEATHER_CHECK = os.getenv('OPEN_WEATHER_CHECK')
OPEN_WEATHER_GEO = os.getenv('OPEN_WEATHER_GEO')
OPEN_WEATHER_CITY = os.getenv('OPEN_WEATHER_CITY')


class WeatherCall:

    def __init__(self, key):
        self.key = key

    def checkKey(self):
        response = requests.get(OPEN_WEATHER_CHECK + self.key)
        if(response.status_code == 401): raise TypeError("invalid Key")

    def get_coordinates(self, city, limit):
        response = requests.get(f"{OPEN_WEATHER_GEO} q={city}&limit={limit}&appid={self.key}")
        if(response.status_code == 401): raise TypeError("error call")
        return response.json()

    def get_weather(self, lat, lon):
        response = requests.get(f"{OPEN_WEATHER_CITY}lat={lat}&lon={lon}&appid={self.key}")
        if(response.status_code == 401): raise TypeError("error call")
        return response.json()
