import requests
from pathlib import Path
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='The script download images from NASA'
    )
    parser.add_argument(
        '--launch_id', '-id', help='Specify the desired launch id'
    )
    return parser


def fetch_spacex_images(path, launch_id):
    api_endpoint = 'https://api.spacexdata.com/v5/launches/{}'
    if launch_id:
        response = requests.get(api_endpoint.format(launch_id))
        response.raise_for_status()
    else:
        response = requests.get(api_endpoint.format('latest'))
        response.raise_for_status()

    links_images = response.json()['links']['flickr']['original']

    if links_images:
        for image_number, image_link in enumerate(links_images, start=1):
            filename = f'spacex_{image_number}'
            download_image(image_link, path, filename)
        else:
            return 'All pictures was download successfully'
    else:
        return 'The list of pictures is empty'


def download_image(url, path, name):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f'{path}/{name}.jpg', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    path = './images'
    parser = create_parser()
    args = parser.parse_args()
    try:
        print(fetch_spacex_images(path, args.launch_id))
    except requests.exceptions.HTTPError:
        print('Ann error occurred. Pictures were not downloaded!')

