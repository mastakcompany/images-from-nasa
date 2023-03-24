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


def run_send_messages(token, chat_id, frequent_time, path):
    bot = telegram.Bot(token=token)
    while True:
        for root, dirs, files in os.walk('images'):
            random.shuffle(files)
            for image in files:
                with open(f'{path}/{image}', 'rb') as photo:
                    bot.send_photo(
                        chat_id,
                        photo=photo
                    )
                sleep(int(frequent_time)*3600)


if __name__ == '__main__':
    load_dotenv()
    path = './images'
    parser = create_parser()
    args = parser.parse_args()
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    run_send_messages(token, chat_id, args.frequence, path)
