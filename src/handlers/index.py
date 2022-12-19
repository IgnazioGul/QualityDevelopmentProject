from telegram import Update, InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import ContextTypes
from uuid import uuid4
from src.weather import WeatherCall
import os
from dotenv import load_dotenv
import logging

from src.services.index import start_service

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# init dot env
load_dotenv()

# Get env variable
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')

async def start(update: Update, context: ContextTypes) -> None:
    """ Sends a message on /start with three inline button attached. """
    logger.info('Start handler %s', context.user_data )
    await start_service(update)



async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Handle the inline query. This is run when you type: @meteounicitbot <query>"""
    query = update.inline_query.query
    print(context.args)

    if query == "":
        return None

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
    'coord': {'lon': float, 'lat': float},
    'weather': [{'id': float, 'main': str, 'description': str, 'icon': str}],
    'base': str,
    'main': {'temp': float, 'feels_like': float, 'temp_min': float, 'temp_max': float, 'pressure': float, 'humidity': float},
    'visibility': float,
    'wind': {'speed': float, 'deg': float},
    'clouds': {'all': float},
    'dt': int,
    'sys': {'type': int, 'id': int, 'country': str, 'sunrise': int, 'sunset': int},
    'timezone': int,
    'id': int,
    'name': str,
    'cod': int}



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


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user for info about the selected predefined choice."""

    text = update.message.text
    coordinate = str(text).split(",")
    meteo = WeatherCall.get_weather(coordinate[0], coordinate[1])

    print(context.args)
    message = get_message(meteo)

    await update.message.reply_text(message)
    