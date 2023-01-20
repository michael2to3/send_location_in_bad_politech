from telethon import types, functions
from telethon.sync import TelegramClient
import time
import schedule
from decouple import config

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
        '@echecs95',
        file=types.InputMediaGeoLive(
            types.InputGeoPoint(0, 0),
            period=60
        )
    )


schedule.every(1).minutes.do(send_live_location)

while True:
    schedule.run_pending()
    time.sleep(1)
