from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup, InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import ContextTypes
from uuid import uuid4
from src.weather import WeatherCall
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Sends a message on /start with three inline button attached. """
    print(context.args)

    keyboard = [[InlineKeyboardButton(
        'Inizia la ricerca', switch_inline_query_current_chat="")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Benvenuto in weater_bot\nrimani aggiornato sul meteo con pochi click', reply_markup=reply_markup)



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

