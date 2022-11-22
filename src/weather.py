import requests
from dotenv import load_dotenv
import os

load_dotenv()

OPEN_WEATHER_CHECK = os.getenv('OPEN_WEATHER_CHECK')
OPEN_WEATHER_GEO = os.getenv('OPEN_WEATHER_GEO')
OPEN_WEATHER_CITY = os.getenv('OPEN_WEATHER_CITY')


class WeatherCall:

    def __init__(self, key: str) -> None:
        self.key = key

    def check_key(self) -> None:
        response = requests.get(OPEN_WEATHER_CHECK + self.key, timeout=10)
        if response.status_code == 401:
            raise TypeError("Invalid Key")

    def get_coordinates(self, city: str, limit: int) -> dict:
        response = requests.get(
            f"{OPEN_WEATHER_GEO}q={city}&limit={limit}&appid={self.key}", timeout=10)
        if response.status_code == 401:
            raise TypeError("Error Call")
        return response.json()

    def get_weather(self, lat: float, lon: float) -> dict:
        response = requests.get(
            f"{OPEN_WEATHER_CITY}lat={lat}&lon={lon}&appid={self.key}", timeout=10)
        if response.status_code == 401:
            raise TypeError("Error Call")
        return response.json()
