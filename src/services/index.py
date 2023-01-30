from telegram import InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardButton, Update, InlineKeyboardMarkup
from src.weather import WeatherCall
import logging
from uuid import uuid4

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


async def start_service(update: Update) -> Update:
    """ Sends a message on /start with three inline button attached. """

    keyboard = [[InlineKeyboardButton(
        'Inizia la ricerca', switch_inline_query_current_chat="")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Benvenuto in weater_bot\nrimani aggiornato sul meteo con pochi click', reply_markup=reply_markup)


async def get_city_by_query(query) -> InlineQueryResultArticle:
    results = []
    locations = []
    try:
        locations = WeatherCall.get_coordinates(query, 5)
    except TypeError:
        pass

    for location in locations:
        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=f"{ location.get('name', '') }, { location.get('state', '') } - { location.get('coutry', '') } ",
                thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Weather-sun-clouds-rain.svg/640px-Weather-sun-clouds-rain.svg.png",
                thumb_width=180,
                thumb_height=180,
                input_message_content=InputTextMessageContent(
                    f"{location['lat']},{location['lon']}"),
            ),
        )

    return results


async def message_service(update: Update) -> Update:
    text = update.message.text
    coordinate = str(text).split(",")
    meteo = WeatherCall.get_weather(coordinate[0], coordinate[1])
    message = get_message(meteo)

    await update.message.reply_text(message)

from typing import Dict, List, Union

MeteoProp = Dict[str, Union[Dict[str, Union[float, int, str]], 
    List[Dict[str, Union[float, int, str]]], float, int, str]]


def get_message(meteo: MeteoProp) -> str:
    if meteo == {}:
        return ""
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
    if 'humidity' in main:
        message += f"umidità: {main['humidity']}% 💧\n"
    if 'sea_level' in main:
        message += f"livello del mare: {main['sea_level']} 🌊\n"

    return message
