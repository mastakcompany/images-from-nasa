import argparse
import os
import random

import telegram
from dotenv import load_dotenv


def get_images(path):
    for root, path, files in os.walk(path):
        return files


def create_parser(path):
    parser = argparse.ArgumentParser(
        description='Space images script'
    )
    parser.add_argument(
        '--photo',
        '-p',
        default=random.choice(get_images(path)),
        help='Specify a photo to be send to the Telegram channel'
    )
    return parser


def send_image(token, chat_id, path, image):
    bot = telegram.Bot(token=token)
    with open(f'{path}/{image}', 'rb') as photo:
        bot.send_photo(
            chat_id,
            photo=photo
        )


if __name__ == '__main__':
    load_dotenv()
    path = './images'
    parser = create_parser(path)
    args = parser.parse_args()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    send_image(token, chat_id, path, args.photo)
