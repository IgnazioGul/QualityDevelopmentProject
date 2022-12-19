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
