import argparse
import os
import random
from time import sleep

import telegram
from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser(
        description='Space images script'
    )
    parser.add_argument(
        '--frequence',
        '-f',
        help='Specify the frequency of publication in hours',
        default=4
    )
    return parser


def send_photo(bot, chat_id, image):
    bot.send_photo(
        chat_id=chat_id,
        photo=image
    )


def run_send_messages(token, chat_id, frequent_time, path):
    bot = telegram.Bot(token=token)
    images = [filenames for *dirpath, filenames in os.walk('./images')][0]
    while True:
        try:
            photo = images.pop()
        except IndexError:
            images = [filenames for *dirpath, filenames in os.walk('./images')][0]
            random.shuffle(images)
        else:
            with open(f'{path}/{photo}', 'rb') as photo:
                send_photo(bot, chat_id, photo)
        sleep(int(frequent_time)*3600)


if __name__ == '__main__':
    load_dotenv()
    path = './images'
    parser = create_parser()
    args = parser.parse_args()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    run_send_messages(token, chat_id, args.frequence, path)
