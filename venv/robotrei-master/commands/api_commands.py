import pyyoutube
from twitchbot import Command
import datetime
import random
import json
import asyncio
import httpx
from pyyoutube import api



# this loads the super secret api keys
try:
    with open('configs/api_keys.json') as f:
        api_keys = json.load(f)
except FileNotFoundError:
    print("[Notice]: creating empty configuration file 'configs/api_keys.json'")
    empty_config = {
        "dictionary": "",
        "weather": "",

        # youtube config not used in this file, but other files
        # depend on it, so lets just write it here
        "youtube_api": "",
    }
    with open('configs/api_keys.json', 'w') as f:
        json.dump(empty_config, f)
        api_keys = empty_config




# dictionary
@Command('define', aliases=['word', 'definition'], cooldown=60)
async def cmd_function(msg, *args):
    if api_keys["dictionary"] == "":
        print("[BOT] !define command: missing api key for 'dictionary'")
        return

    custom_word = "+".join(args)

    url = f"https://wordsapiv1.p.rapidapi.com/words/{custom_word}/definitions"

    headers = {
        'x-rapidapi-key': api_keys['dictionary'],
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

    # TODO error handling
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    data = response.json()
    if response.status_code == 200:
        definition = random.choice(data['definitions'])['definition']
        await msg.reply(f' the definition of {custom_word} might be: "{definition}"')
    else:
        message = data['message']
        await msg.reply(f'sadly {message}')


# bitcoin
@Command('bitcoin', aliases=['bit', 'b'])
async def cmd_function(msg, *args):
    # TODO error handling
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.bybit.com/v2/public/tickers?btcusd')

    data = response.json()
    btc_price_usd = data['result'][0]['last_price']
    await msg.reply(f'the current price of bitcoin is: ${btc_price_usd} ')


# eth
@Command('ethereum', aliases=['eth'])
async def cmd_function(msg, *args):
    # TODO error handling
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.bybit.com/v2/public/tickers?ethusd')

    data = response.json()
    eth_price_usd = data['result'][1]['last_price']
    await msg.reply(f'the current price of ethereum is: ${eth_price_usd} ')

@Command('bitcoincash', aliases=['bch'])
async def cmd_function(msg, *args):
    # TODO error handling
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.bybit.com/v2/public/tickers?BCHUSDT')

    data = response.json()
    bch_price_usd = data['result'][5]['last_price']
    await msg.reply(f'the current price of bitcoin cash is: ${bch_price_usd} ')

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
    if api_keys["weather"] == "":
        print("[BOT] !weather command: missing api key for 'weather'")
        return

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
        async with httpx.AsyncClient() as client:
            response = await client.get(request_url)
    except httpx.HTTPError:

        # TODO this error message is not correct.
        # this exception is for _any_ failure of the api call
        # (not just if the city name is bad)
        await msg.reply(f'It seems you have not provided a useful city name, please try again later ')

    data = response.json()
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
        f'{msg_prefix}The weather in {city_display_name} is {description}. The current temperature is {temp}C, it feels like {feels_like}C (its {dumb_units} in dumb fahrenheit). The sun will set at {sunset} but it will rise again at {sunrise} in local time.')



# jokes
@Command('joke', aliases=['dadjoke'])
async def cmd_function(msg, *args):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://official-joke-api.appspot.com/random_joke')
    except httpx.HTTPError:
        await msg.reply("There was an error calling the joke api")
        return
    
    joke = response.json()
    setup = joke['setup']
    punchline = joke['punchline']
    await msg.reply(setup)
    await asyncio.sleep(2)
    await msg.reply(punchline)
