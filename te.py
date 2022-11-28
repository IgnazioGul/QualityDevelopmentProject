from src.weather import WeatherCall
from pytest_mock import MockerFixture
from dotenv import load_dotenv
import os
load_dotenv()
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')
def test_checkKey():
    pass

def test_coordinates_full():
    #arrage
    
    #act
    res = WeatherCall.get_coordinates('roma', 3)
    lat,lon = res[0]['lat'], res[0]['lon']
    res2 = WeatherCall.get_weather(lat, lon)
    print(lat, lon, res2)

    #assert
    
   

test_coordinates_full()