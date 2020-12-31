import pyyoutube
from twitchbot import Command
import datetime
import random
from urllib.request import urlopen
from urllib.error import HTTPError
import json
import asyncio
import requests
from pyyoutube import api


# this loads the super secret api keys
with open('configs/api_keys.json') as f:
    api_keys = json.load(f)



# dictionary
@Command('define', aliases=['word'], cooldown=60)
async def cmd_function(msg, *args):
    custom_word = "+".join(args)

    url = f"https://wordsapiv1.p.rapidapi.com/words/{custom_word}/definitions"

    headers = {
        'x-rapidapi-key': api_keys['dictionary'],
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()
    if response.status_code == 200:
        definition = random.choice(data['definitions'])['definition']
        await msg.reply(f' lisare1Robot the definition of {custom_word} might be: "{definition}"')
    else:
        message = data['message']
        await msg.reply(f'sadly {message}')


# bitcoin
@Command('bitcoin', aliases=['bit', 'b'])
async def cmd_function(msg, *args):
    btc_price_usd = json.loads(urlopen('https://api.bybit.com/v2/public/tickers?btcusd').read())['result'][0][
        'last_price']
    await msg.reply(f'the current price of bitcoin is: ${btc_price_usd} lisare1Arson')


# eth
@Command('ethereum', aliases=['eth'])
async def cmd_function(msg, *args):
    eth_price_usd = json.loads(urlopen('https://api.bybit.com/v2/public/tickers?ethusd').read())['result'][1][
        'last_price']
    await msg.reply(f'the current price of ethereum is: ${eth_price_usd} lisare1Hiss')


# weather

OPEN_WEATHER_APPID = api_keys['weather']
OPEN_WEATHER_UNITS = 'metric'
OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/{}?q={}&appid={}&units={}'
# OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/{operation}?q={city}&appid={app_id}&units={units}'
# you can use above variable when you want to manually specify the fields while formatting the string, otherwise always follow the order from left to right
OW_OPERATION_WEATHER = 'weather'
OW_OPERATION_FORECAST = 'forecast'


# added weather stuff kelvins--> metric WEATHER, FUCKING TIMEZONES
@Command('weather', aliases=['cold'])
async def cmd_function(msg, *args):
    # determine city_api_name, city_display_name beforehand to avoid code duplication
    if not args:
        # No args -> Assume Prague
        city_api_name = city_display_name = city_test_name = 'Prague'
        msg_prefix = 'For Lisa, '
    else:
        city_display_name = ' '.join(args).title()
        city_api_name = '+'.join(args)
        city_test_name = ''.join(args)
        msg_prefix = ''

    # generate URL with the required inputs
    request_url = OPEN_WEATHER_URL.format(OW_OPERATION_WEATHER, city_api_name, OPEN_WEATHER_APPID, OPEN_WEATHER_UNITS)

    # we're ready now, lets hit the OPEN-WEATHER API!
    try:
        response = urlopen(request_url)
        data = json.loads(response.read())
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        feels_like = data['main']['feels_like']
        dumb_units = round(((temp * 1.8) + 32), 2)
        timezone = data['timezone']
        # sunset
        sunset_raw = data['sys']['sunset']
        sunset_convert = sunset_raw + timezone
        sunset = datetime.datetime.fromtimestamp(sunset_convert).strftime('%H:%M')
        # sunrise
        sunrise_raw = data['sys']['sunrise']
        sunrise_convert = sunrise_raw + timezone
        sunrise = datetime.datetime.fromtimestamp(sunrise_convert).strftime('%H:%M')

        await msg.reply(
            f'{msg_prefix}The weather in {city_display_name} is {description} lisare1Robot  The current temperature is {temp} celsius, it feels like {feels_like} celsius but its {dumb_units} in dumb fahrenheit lisare1Hiss  Also, the sun will set at {sunset} but it will rise again at {sunrise} in local time lisare1Arson ')

    # API call was not a success
    except HTTPError:
        await msg.reply(f'It seems you have not provided a useful city name, please try again later lisare1Hiss ')



# jokes
@Command('joke', aliases=['dadjoke'])
async def cmd_function(msg, *args):
    joke = json.loads(urlopen('https://official-joke-api.appspot.com/random_joke').read())
    setup = joke['setup']
    punchline = joke['punchline']
    await msg.reply(setup)
    await asyncio.sleep(2)
    await msg.reply(punchline)
