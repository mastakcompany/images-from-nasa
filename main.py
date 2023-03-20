import datetime
import os
from pathlib import Path
from urllib.parse import urlsplit
from os.path import splitext
import random
import requests
from dotenv import load_dotenv


def download_image(url, path, name):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f'{path}/{name}.jpg', 'wb') as file:
        file.write(response.content)


def fetch_apod_images(path, api_key):
    api_endpoint = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': random.randint(30, 50)
    }
    response = requests.get(api_endpoint, params=params)
    response.raise_for_status()
    apods_list = response.json()

    for apods_number, apod in enumerate(apods_list, start=1):
        filename = f'spacex_{apods_number}'
        pictures_url = apod['url']
        try:
            download_image(pictures_url, path, filename)
        except requests.exceptions.HTTPError:
            print('The picture not download')
    else:
        print('All APOD pictures was download successfully')


def fetch_epic_images(path, api_key):
    api_endpoint = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png?api_key={}'
    list_of_image_objects = 'https://api.nasa.gov/EPIC/api/natural/images?api_key={}'
    response = requests.get(list_of_image_objects.format(api_key))
    response.raise_for_status()
    for image_object in response.json():
        image_name = image_object['image']
        image_date = datetime.date.fromisoformat(image_object['date'].split()[0]).strftime('%Y/%m/%d')
        picture_url = api_endpoint.format(image_date, image_name, api_key)
        try:
            download_image(picture_url, path, image_name)
        except requests.exceptions.HTTPError:
            print('The picture not download')
    else:
        print('All EPIC pictures was download successfully')


def get_file_extension(url):
    return splitext(urlsplit(url).path)[1]


if __name__ == '__main__':
    path = './images'
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    fetch_epic_images(path, token)
    fetch_apod_images(path, token)
