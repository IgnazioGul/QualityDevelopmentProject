from telegram import Update
from telegram.ext import ContextTypes
import logging
from src.services.index import start_service, get_city_by_query, message_service

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes) -> None:
    """ Sends a message on /start with three inline button attached. """
    logger.info('Start handler %s', context.user_data )
    await start_service(update)



async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Handle the inline query. This is run when you type: @meteounicitbot <query>"""
    query = update.inline_query.query
    logger.info('inline query handler %s', context.user_data )

    if query == "":
        return None

    results = await get_city_by_query(query)
    await update.inline_query.answer(results)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Ask the user for info about the selected predefined choice."""

    logger.info('Message handler %s', context.user_data )
    await message_service(update)
    