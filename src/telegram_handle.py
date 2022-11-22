from telegram import InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from uuid import uuid4
from src.weather import WeatherCall
import os
from dotenv import load_dotenv

# init dot env
load_dotenv()

# Get env variable
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')

# initialize weatherCall instance
weatherCall = WeatherCall(OPEN_WEATHER_KEY)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Sends a message with three inline button attached. """

    keyboard = [[InlineKeyboardButton(
        'Inizia la ricerca', switch_inline_query_current_chat="")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Benvenuto in weater_bot, rimani aggiornato sul meteo con pochi click', reply_markup=reply_markup)


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @meteounicitbot <query>"""
    query = update.inline_query.query

    if query == "":
        return

    results = []
    locations = weatherCall.get_coordinates(query)
  
    for location in locations:
        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=f"{ location['name'] if 'name' in location else '' }, { location['state'] if 'state' in location else '' } - { location['country'] if 'state' in location else '' } ",
                thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Weather-sun-clouds-rain.svg/640px-Weather-sun-clouds-rain.svg.png",
                thumb_width=180,
                thumb_height=180,
                input_message_content=InputTextMessageContent(query.upper()),
            ),
        )

    await update.inline_query.answer(results)
