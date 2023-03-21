import os

import telegram
from dotenv import load_dotenv


def sent_message(token, chat_id):
    bot = telegram.Bot(token=token)
    bot.send_message(
        text='Hi! This is the test message.',
        chat_id=chat_id
    )


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    sent_message(token, chat_id)
