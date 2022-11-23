import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPEN_WEATHER_CHECK = os.getenv('OPEN_WEATHER_CHECK')
OPEN_WEATHER_GEO = os.getenv('OPEN_WEATHER_GEO')
OPEN_WEATHER_CITY = os.getenv('OPEN_WEATHER_CITY')


class WeatherCall:

    def __init__(self, key: str) -> None:
        self.key = key

    def check_key(self) -> None:
        """
        check_key method checks if the key is correct for the API call
        :return:  if the error occurs, the method returns an exception
        """
        response = requests.get(OPEN_WEATHER_CHECK + self.key, timeout=10)
        if response.status_code == 401:
            raise TypeError("Invalid Key")

    def get_coordinates(self, city: str, limit: int) -> dict | None:
        """
        the get_coordinates method executes an API call which, given a city, returns its coordinates
        :param city: the city taken to have its coordinates
        :param limit:the maximum number of values chosen
        :return: the json containing the coordinates
        """
        response = requests.get(f"{OPEN_WEATHER_GEO}q={city}&limit={limit}&appid={self.key}", timeout=10)
        if response.status_code == 401:
            raise TypeError("Error Call")
        return response.json()

    def get_weather(self, lat: float, lon: float) -> dict | None:
        """
        the get_weather method executes an API call which, given latitude and longitude, returns its weather
        :param lat: latitude
        :param lon: longitude
        :return: the json containing all the information on the weather of the city
        """
        response = requests.get(f"{OPEN_WEATHER_CITY}lat={lat}&lon={lon}&appid={self.key}", timeout=10)
        if response.status_code == 401:
            raise TypeError("Error Call")
        return response.json()
