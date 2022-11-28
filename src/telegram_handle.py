from telegram import InputTextMessageContent, InlineQueryResultArticle, Update
from telegram.ext import ContextTypes, ConversationHandler
from uuid import uuid4
from .weather import WeatherCall
import os
from dotenv import load_dotenv
import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# init dot env
load_dotenv()

# Get env variable
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')



async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Handle the inline query. This is run when you type: @meteounicitbot <query>"""
    query = update.inline_query.query
    print ( context.args)

    if query == "":
        return

    results = []
    locations = None
    try:
        locations = WeatherCall.get_coordinates(query, 5)
    except TypeError:
        locations = []

    for location in locations:
        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=f"{ location['name'] if 'name' in location else '' }, { location['state'] if 'state' in location else '' } - { location['country'] if 'state' in location else '' } ",
                thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Weather-sun-clouds-rain.svg/640px-Weather-sun-clouds-rain.svg.png",
                thumb_width=180,
                thumb_height=180,
                input_message_content=InputTextMessageContent(
                    f"{location['lat']},{location['lon']}"),
            ),
        )

    await update.inline_query.answer(results)


meteo_prop = {
    'coord': {'lon': 15.0874, 'lat': 37.5024},
    'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
    'base': 'stations',
    'main': {'temp': 18.86, 'feels_like': 18.79, 'temp_min': 16, 'temp_max': 21.38, 'pressure': 1014, 'humidity': 76},
    'visibility': 10000,
    'wind': {'speed': 2.06, 'deg': 0},
    'clouds': {'all': 0},
    'dt': 1669279345,
    'sys': {'type': 2, 'id': 2004061, 'country': 'IT', 'sunrise': 1669268916, 'sunset': 1669304660},
    'timezone': 3600,
    'id': 2525068,
    'name': 'Catania',
    'cod': 200}


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user for info about the selected predefined choice."""

    text = update.message.text
    coordinate = str(text).split(",")
    meteo = WeatherCall.get_weather(coordinate[0], coordinate[1])

    print ( context.args)
    message = get_message(meteo)

    await update.message.reply_text(message)

def get_message(meteo: meteo_prop) -> str:
    main = meteo['main']
    message = ""
    if 'name' in meteo:
        message += f"Che tempo fa a {meteo['name']}?\n"
    if 'temp' in main:
        message += f"temp.: {main['temp']} C° 🌡\n"
    if 'feels_like' in main:
        message += f"temp. avvertita: {main['feels_like']} C° 🌡\n"
    if 'temp_min' in main:
        message += f"temp. min: {main['temp_min']} C° 🧊\n"
    if 'temp_max' in main:
        message += f"temp. max: {main['temp_max']} C° 🔥\n"
    if 'pressure' in main:
        message += f"pressione: {main['pressure']}\n"
    if 'temp_max' in main:
        message += f"umidità: {main['humidity']}% 💧\n"
    if 'sea_level' in main:
        message += f"livello del mare: {main['sea_level']} 🌊\n"

    return message
