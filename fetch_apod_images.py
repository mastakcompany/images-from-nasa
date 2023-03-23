import os
import random
import requests
from dotenv import load_dotenv
import argparse

from utils import download_image


def create_parser():
    parser = argparse.ArgumentParser(
        description='The script download images from NASA'
    )
    parser.add_argument(
        '--count', '-c', help='Specify count of pictures. Random if not set.',
        default=random.randint(1, 10)
    )
    return parser


def fetch_apod_images(count, path, api_key):
    api_endpoint = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count
    }
    response = requests.get(api_endpoint, params=params)
    response.raise_for_status()
    apods_list = response.json()

    for apods_number, apod in enumerate(apods_list, start=1):
        filename = f'apod_{apods_number}'
        pictures_url = apod['url']
        try:
            download_image(pictures_url, path, filename)
        except requests.exceptions.HTTPError:
            return 'The image was not downloaded'
    else:
        return 'All APOD images were successfully downloaded'


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    path = './images'
    parser = create_parser()
    args = parser.parse_args()
    print(fetch_apod_images(args.count, path, token))
