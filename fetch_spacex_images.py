import requests
import argparse

from utils import download_image


def create_parser():
    parser = argparse.ArgumentParser(
        description='The script download images from NASA'
    )
    parser.add_argument(
        '--launch_id', '-id', help='Specify the desired launch id',
        default='latest'
    )
    return parser


def fetch_spacex_images(path, launch_id):
    api_endpoint = 'https://api.spacexdata.com/v5/launches/{}'
    response = requests.get(api_endpoint.format(launch_id))
    response.raise_for_status()

    links_images = response.json()['links']['flickr']['original']

    if not links_images:
        return 'The list of pictures is empty'
    else:
        for image_number, image_link in enumerate(links_images, start=1):
            filename = f'spacex_{image_number}'
            download_image(image_link, path, filename)
        return 'All pictures were download successfully'


if __name__ == '__main__':
    path = './images'
    parser = create_parser()
    args = parser.parse_args()
    try:
        print(fetch_spacex_images(path, args.launch_id))
    except requests.exceptions.HTTPError:
        print('Ann error occurred. Pictures were not downloaded!')

