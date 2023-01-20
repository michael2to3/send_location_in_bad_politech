# Telegram Live Location Sender

This repository contains a Python script that sends live location to Telegram.

## Requirements
- Python 3.9+
- telethon library

## Installation
- Clone the repository
- Run `pip install -r requirements.txt` to install the dependencies
- Replace `YOUR_API_ID`, `YOUR_API_HASH`, `YOUR_SESSION_NAME`, `YOUR_USERNAME` and `YOUR_PHONE_NUMBER` in the `main.py` script with your own values

## Usage
- Run `python main.py` to send live location

## Docker
- Build the container using the command `docker build -t your_image_name .`
- Run the container using the command `docker run your_image_name`

## Docker compose
- Run with docker compose using the command `docker-compose up -d --build`

## Scheduling
- Use a library such as `schedule` to run the script every 30 minutes

## Authors
- [Michael](https://github.com/michael2to3)
