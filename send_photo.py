import argparse
import os
import random

import telegram
from dotenv import load_dotenv
from main import send_photo


def create_parser():
    parser = argparse.ArgumentParser(
        description='Space images script'
    )
    parser.add_argument(
        '--photo',
        '-p',
        help='Specify a photo to be send to the Telegram channel'
    )
    return parser


def send_image(token, chat_id, path, image):
    bot = telegram.Bot(token=token)
    images = list(os.walk('./images'))[0][2]
    # Здесь я не знаю как можно обойтись дефолтным значением из argparse
    if not image:
        photo = images[random.randint(0, len(images)-1)]
    else:
        photo = image
    with open(f'{path}/{photo}', 'rb') as photo:
        send_photo(bot, chat_id, photo)


if __name__ == '__main__':
    load_dotenv()
    path = './images'
    parser = create_parser()
    args = parser.parse_args()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    send_image(token, chat_id, path, args.photo)
