import requests

class WeatherCall:

    def __init__(self, key):
        self.key = key

    def get_coordinates(self, city):
        response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={self.key}')
        if(response.json() == []): return None
        else: return response.json()

    def get_weather(self, lat, lon):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.key}")
        if(response.json() == []): return None
        else: return response.json()['weather']
