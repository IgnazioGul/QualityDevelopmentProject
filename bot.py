import os
import logging
from configparser import ConfigParser
from dotenv import load_dotenv
from telegram.ext import CommandHandler, ApplicationBuilder, InlineQueryHandler, MessageHandler, filters
from src.handlers.index import start, inline_query, message_handler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# init dot env
load_dotenv()

constants = ConfigParser()
constants.read("constants.ini")
load_dotenv()

# Get env variable
TELEGRAM_BOT_TOKEN = os.getenv(constants.get('KEY', 'TELEGRAM_BOT_TOKEN_NAME'))

def main() -> None:
    """Run the bot."""
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(InlineQueryHandler(inline_query))
    app.add_handler(MessageHandler(filters.Regex(r"^(-?\d+(\.\d+)?),\s*(-?\d+(\.\d+)?)$"), message_handler))

    app.run_polling()

if __name__ == '__main__':
    main()
