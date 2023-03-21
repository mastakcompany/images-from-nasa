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
        help='Specify the frequency of publication in hours'
    )
    return parser


def send_photo(bot, chat_id, image):
    bot.send_photo(
        chat_id=chat_id,
        photo=image
    )


def main(token, chat_id, frequent_time, path):
    bot = telegram.Bot(token=token)
    images = list(os.walk('./images'))[0][2]
    if not frequent_time:
        frequent_time = 4
    while True:
        try:
            photo = images.pop()
        except IndexError:
            images = list(os.walk('./images'))[0][2]
            random.shuffle(images)
        else:
            with open(f'{path}/{photo}', 'rb') as photo:
                send_photo(bot, chat_id, photo)
        print(frequent_time)
        sleep(int(frequent_time)*3600)


if __name__ == '__main__':
    load_dotenv()
    path = './images'
    parser = create_parser()
    args = parser.parse_args()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    main(token, chat_id, args.frequence, path)
