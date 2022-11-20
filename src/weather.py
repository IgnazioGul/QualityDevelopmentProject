import requests

class WeatherCall:

    def __init__(self, key):
        self.key = key

    def checkKey(self):
        response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={self.key}")
        if(response.status_code == 401): raise TypeError("invalid Key")

    def get_coordinates(self, city):
        response = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={self.key}")
        if(response.json() == []): return None
        else: return response.json()

    def get_weather(self, lat, lon):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.key}")
        if(response.json() == []): return None
        else: return response.json()
