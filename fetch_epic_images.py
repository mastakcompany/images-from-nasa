import datetime
import os
import requests
from dotenv import load_dotenv

from utils import download_image


def fetch_epic_images(path, api_key):
    payload = {
        'api_key': api_key
    }
    api_endpoint = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'
    images = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(
        images,
        params=payload
    )
    response.raise_for_status()
    for image in response.json():
        image_name = image['image']
        image_date = datetime.date.fromisoformat(image['date'].split()[0]).strftime('%Y/%m/%d')
        picture_url = api_endpoint.format(image_date, image_name)
        download_image(picture_url, path, image_name, api_key)
    else:
        return 'All EPIC images were successfully downloaded'


if __name__ == '__main__':
    path = './images'
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    try:
        print(fetch_epic_images(path, token))
    except requests.exceptions.HTTPError:
        print('An error occurred. Pictures were not downloaded!')
