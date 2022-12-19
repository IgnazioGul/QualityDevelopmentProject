from telegram import InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardButton, Update, InlineKeyboardMarkup
from src.weather import WeatherCall
import logging
from uuid import uuid4

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


async def start_service(update: Update):
    """ Sends a message on /start with three inline button attached. """

    keyboard = [[InlineKeyboardButton(
        'Inizia la ricerca', switch_inline_query_current_chat="")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Benvenuto in weater_bot\nrimani aggiornato sul meteo con pochi click', reply_markup=reply_markup)


async def get_city_by_query(query):
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

    return results
