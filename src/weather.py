import os
from dotenv import load_dotenv
import requests

load_dotenv()
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')
OPEN_WEATHER_CHECK = os.getenv('OPEN_WEATHER_CHECK')
OPEN_WEATHER_GEO = os.getenv('OPEN_WEATHER_GEO')
OPEN_WEATHER_CITY = os.getenv('OPEN_WEATHER_CITY')

class WeatherCall:

    @staticmethod
    def check_key() -> str | TypeError:
        """
        check_key method checks if the key is correct for the API call
        :return:  if the error occurs, the method returns an exception
        """
        response = WeatherCall.check(OPEN_WEATHER_KEY)
        if response == '401':
            raise TypeError("Invalid Key")
        return response

    @staticmethod
    def get_coordinates(city: str, limit: int) -> dict | TypeError:
        """
        the get_coordinates method executes an API call which, given a city, returns its coordinates
        :param city: the city taken to have its coordinates
        :param limit:the maximum number of values chosen
        :return: the json containing the coordinates
        """
        response = WeatherCall.geo_response(OPEN_WEATHER_KEY, city, limit)
        if "cod" in response:
            raise TypeError("Error Call")
        return response

    @staticmethod
    def get_weather(lat: float, lon: float) -> dict | TypeError:
        """
        the get_weather method executes an API call which, given latitude and longitude, returns its weather
        :param lat: latitude
        :param lon: longitude
        :return: the json containing all the information on the weather of the city
        """
        response = WeatherCall.weather_response(OPEN_WEATHER_KEY, lat, lon)
        if "cod" in response and response['cod'] != 200:
            raise TypeError("Error Call")
        return response

    @staticmethod
    def check(key: str) -> str:
        res = requests.get(OPEN_WEATHER_CHECK + key, timeout=10).json()['cod']
        return res

    @staticmethod
    def geo_response(key: str, city: str, limit: int) -> dict:
        res = requests.get(f"{OPEN_WEATHER_GEO}q={city}&limit={limit}&appid={key}", timeout=10).json()
        return res

    @staticmethod
    def weather_response(key: str, lat: float, lon: float) -> dict:
        res = requests.get(f"{OPEN_WEATHER_CITY}lat={lat}&lon={lon}&units=metric&appid={key}", timeout=10).json()
        return res
