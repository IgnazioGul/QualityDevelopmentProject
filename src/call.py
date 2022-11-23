import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPEN_WEATHER_CHECK = os.getenv('OPEN_WEATHER_CHECK')
OPEN_WEATHER_GEO = os.getenv('OPEN_WEATHER_GEO')
OPEN_WEATHER_CITY = os.getenv('OPEN_WEATHER_CITY')


def check(key):
    res = requests.get(OPEN_WEATHER_CHECK + key, timeout=10).json()['cod']
    return res

def geo(key,city,limit):
    res = requests.get(f"{OPEN_WEATHER_GEO}q={city}&limit={limit}&appid={key}", timeout=10).json()
    return res

def weather(key,lat,lon):
    res = requests.get(f"{OPEN_WEATHER_CITY}lat={lat}&lon={lon}&appid={key}", timeout=10).json()
    return res
