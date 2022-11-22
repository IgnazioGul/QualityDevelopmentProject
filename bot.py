import os
import logging
from dotenv import load_dotenv
from telegram.ext import CommandHandler, ApplicationBuilder, InlineQueryHandler
from src.telegram_handle import start, inline_query

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# init dot env
load_dotenv()

# Get env variable
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


def main() -> None:
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(InlineQueryHandler(inline_query))

    app.run_polling()


if __name__ == '__main__':
    main()
