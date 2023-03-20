import datetime
import os
import requests
from dotenv import load_dotenv

from main import download_image


def fetch_epic_images(path, api_key):
    api_endpoint = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png?api_key={}'
    list_of_image_objects = 'https://api.nasa.gov/EPIC/api/natural/images?api_key={}'
    response = requests.get(list_of_image_objects.format(api_key))
    response.raise_for_status()
    for image_object in response.json():
        image_name = image_object['image']
        image_date = datetime.date.fromisoformat(image_object['date'].split()[0]).strftime('%Y/%m/%d')
        picture_url = api_endpoint.format(image_date, image_name, api_key)
        download_image(picture_url, path, image_name)
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
