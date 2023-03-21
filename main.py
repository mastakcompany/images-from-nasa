import os

import telegram
from dotenv import load_dotenv


def sent_message(bot, chat_id):
    bot.send_message(
        text='Hi! This is the test message.',
        chat_id=chat_id
    )


def send_photo(bot, chat_id):
    bot.send_photo(
        chat_id=chat_id,
        photo=open('./images/epic_1b_20230319152855.jpg', 'rb')
    )


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    bot = telegram.Bot(token=token)
    send_photo(bot, chat_id)

