from telethon import types, functions
from telethon.sync import TelegramClient
import time
import schedule
from decouple import config
from random import randint

api_id = config('API_ID')
api_hash = config('API_HASH')
session_name = config('SESSION_NAME')
phone_number = config('PHONE_NUMBER')
auth_code = config('AUTH_CODE')

chat_id = 1928159074

client = TelegramClient('session_name', api_id, api_hash)

client.start(phone_number, auth_code)

def send_live_location():
    client.send_message(
        '@poly_chess_bot',
        file=types.InputMediaGeoLive(
            types.InputGeoPoint(59.965128, 30.398474),
            period=60
        )
    )


send_live_location()
schedule.every(30).minutes.do(send_live_location)

while True:
    schedule.run_pending()
    time.sleep(1 + randint(30,60))
