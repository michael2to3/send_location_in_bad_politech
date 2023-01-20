# Telegram Live Location Sender

This repository contains a Python script that sends live location to Telegram.

## Requirements
- Python 3.9+
- telethon library
- schdule library

## Installation
- Clone the repository
- Run `pip install -r requirements.txt` to install the dependencies
- Replace `YOUR_API_ID`, `YOUR_API_HASH`, `YOUR_SESSION_NAME`, `YOUR_USERNAME` and `YOUR_PHONE_NUMBER` in the `docker-compose.yml` or `main.py`

## Telegram API
- You need to create an API client to use this script. You can do it by following these steps:
  1. Go to [my.telegram.org](https://my.telegram.org/)
  2. Log in using your Telegram account
  3. Click on `API Development Tools`
  4. Fill in the required fields and create your API client
  5. Replace `YOUR_API_ID` and `YOUR_API_HASH` in the `docker-copose.yml` or `main.py`

## Usage
- Run `python main.py` to send live location
- Or you can use docker

## Docker
- Build the container using the command `docker build -t your_image_name .`
- Run the container using the command `docker run your_image_name`

## Docker compose
- Run with docker compose using the command `docker-compose up -d --build`

## Scheduling
- Use a library such as `schedule` to run the script every 30 minutes

## Authors
- [Michael](https://github.com/michael2to3)
