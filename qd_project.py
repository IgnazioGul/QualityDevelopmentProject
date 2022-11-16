from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to QD exam homepage! Credits to Maugeri, Giancarmelo, Ignazio"

'''
    API to fetch today weather for city
    URL param: city (string)
'''
@app.route("/weather/<string:city>")
def get_weather(city: str):
    # TODO: do your API call here..
    return f'La citta selezionata è {city}!!'