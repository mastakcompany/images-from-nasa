# Images From NASA

Images From NASA is a set of Python scripts that allow users to upload images from the NASA Image Library. It can also be used to send photos to Telegram channels.

# Prerequisites
Before using this script, make sure you have the following installed on your computer:

* Python 3.x
* pip package manager

# Usage

The program includes several scripts that can be used as stand-alone.

## fetch_apod_images.py

This script allows you to fetch the Astronomy Picture of the Day (APOD) images from the NASA API and store them in a local directory.

### Requirements
Before running the script, you need to have Python 3 installed on your computer. You also need to have the requests and dotenv Python packages installed. You can install them by running the following command in your terminal:
```
pip install requests dotenv
```
### Setup
1. Obtain a NASA API key from NASA Open APIs.
2. Create a file named .env in the root of the project directory and add the following line:
```
NASA_TOKEN=your_api_key
```
Replace your_api_key with your actual API key.
### Running the Script
To run the script, open your terminal and navigate to the directory containing the script file. Then, run the following command:
```
python fetch_apod_images.py
```
This will download a random number of images (between 10 and 20) to the ./images directory. If you want to download a specific number of images, you can use the --count or -c argument followed by the desired number:
```
python fetch_apod_images.py --count 5
```
This will download 5 images to the ./images directory.

If the script encounters an error while downloading an image, it will return the message "The image was not downloaded". If all images are downloaded successfully, it will return the message "All APOD images were successfully downloaded".

## fetch_epic_images.py

### Prerequisites
Before running the script, you need to have Python 3 installed on your computer. You also need to have the requests and dotenv Python packages installed. You can install them by running the following command in your terminal:
```
pip install requests dotenv
```
### Setup
1. Obtain a NASA API key from NASA Open APIs.
2. Create a file named .env in the root of the project directory and add the following line:
```
NASA_TOKEN=your_api_key
```
Replace your_api_key with your actual API key.
### Running the Script
To run the script, open your terminal and navigate to the directory containing the script file. Then, run the following command:
```
python fetch_epic_images.py
```
This will download all available natural color images from the EPIC archive to the ./images directory.

If the script encounters an error while downloading an image, it will return the message "An error occurred. Pictures were not downloaded!". If all images are downloaded successfully, it will return the message "All EPIC images were successfully downloaded".

## fetch_spacex_images.py
This script downloads images of SpaceX rockets launches from the SpaceX REST API.

### Usage
To use the script, follow these steps:
1. Clone the repository:
```
git clone https://github.com/mastakcompany/images-from-nasa.git
```
2. Navigate to the script's directory:
```angular2html
cd images-from-nasa
```
3. Install the required packages listed in the requirements.txt file:
```angular2html
pip install -r requirements.txt
```
4. Run the script:
```angular2html
python fetch_spacex.py --launch_id <id>
```
Note that the --launch_id argument is optional. If not provided, the script will download images from the latest SpaceX rocket launch.
### Arguments
The fetch_spacex.py script accepts the following arguments:
--launch_id, -id: specify the desired launch id

### Examples
To download images from the latest SpaceX rocket launch:
```angular2html
python fetch_spacex.py
```
To download images from a specific SpaceX rocket launch, use the launch's id:
```angular2html
python fetch_spacex.py --launch_id <id>
```
### Output
The script downloads the images to a directory named ./images. The file names of the images will be in the format spacex_<image_number>.jpg. If the list of pictures is empty, the script will return a message indicating that the list is empty. If there is an error downloading the images, the script will return an error message.

## send_photo.py
This script allows you to send space images to a Telegram channel using Telegram's API.
### Setup
1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages listed in the requirements.txt file by running pip install -r requirements.txt.
4. Create a .env file in the root directory and add your Telegram API token and channel ID. For example:
```
TELEGRAM_TOKEN=<your_telegram_api_token>
TELEGRAM_CHANNEL_ID=<your_telegram_channel_id>
```
5. Put your space images in the images directory.

### Usage
To use the script, run the following command:
```
python main.py --photo [photo_name]
```
* If --photo is not specified, a random image will be selected from the images directory.
* If --photo is specified, the script will send the specified photo to the Telegram channel.

Note: The script assumes that your photos are located in the images directory. If your photos are located in a different directory, modify the path variable.

## main.py
This is the main script of the program. It allows you to send space images from a folder to a Telegram channel. You can specify the frequency of publication in hours.

### Prerequisites
* Python 3.6 or higher
* Telegram Bot token
* Telegram Channel ID
* Space images in a folder named 'images'

### Installation
1. Clone this repository to your local machine
```
git clone https://github.com/your-username/telegram-space-images-script.git
```
2. Install the required packages
```angular2html
pip install python-telegram-bot python-dotenv
```

### Usage
1. Add your Telegram Bot token and Channel ID to a .env file in the root of the project
```
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHANNEL_ID=your_telegram_channel_id
```
2. Place your space images in a folder named 'images' in the root of the project
3. Run the script
```
python main.py --frequence <frequency_in_hours>
```
* The --frequence or -f argument is optional. If not specified, the default frequency is 4 hours.
4. Enjoy your space images on your Telegram channel!

