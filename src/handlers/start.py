from telegram import InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Sends a message on /start with three inline button attached. """

    keyboard = [[InlineKeyboardButton(
        'Inizia la ricerca', switch_inline_query_current_chat="")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Benvenuto in weater_bot\nrimani aggiornato sul meteo con pochi click', reply_markup=reply_markup)
