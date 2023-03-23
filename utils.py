from pathlib import Path
from urllib.parse import urlsplit
from os.path import splitext
import requests


def download_image(url, path, name, api_key=None):
    payload = {
        'api_key': api_key
    }
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(f'{path}/{name}.jpg', 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    return splitext(urlsplit(url).path)[1]
