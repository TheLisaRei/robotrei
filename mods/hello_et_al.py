from twitchbot import event_handler, Command, Event, Message
from datetime import datetime, timedelta
import re
import random

# candy
# initialize the variable
lastCandyTime = datetime.min


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    if 'candy' in msg.content:
        global lastCandyTime

        currentTime = datetime.now()
        allowedTime = lastCandyTime + timedelta(seconds=60)
        # compare the candyTime variable to current timestamp

        print(currentTime > allowedTime)

        if currentTime > allowedTime:
            lastCandyTime = currentTime
            await msg.reply('i would like some candy...')


# add content- France bullying
lastFrogTime = datetime.min


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    frog_words = ['france', 'french', 'paris', 'baguette']
    message_frog_words = [w.lower() for w in msg.content.split()]
    for frog_w in message_frog_words:
        if frog_w in frog_words:

            global lastFrogTime
            currentTime = datetime.now()
            allowedTime = lastFrogTime + timedelta(seconds=300)

            if currentTime > allowedTime:
                lastFrogTime = currentTime
            await msg.reply(frog_options(msg))


def frog_options(msg):
    frog_reactions = ['Why do French People eat snails? ...because they dont like fast food!',
                      ' Did you hear about the brave Frenchman? ... Oh you didnt? Well dont feel bad no one else has either',
                      'What do French recruits learn in basic training? ...how to surrender in 17 different languages.']
    return random.choice(frog_reactions)





# eve hellos and all - write different ones to cycle thru
last_o7_time = {}


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_o7_time.get(key, datetime.now())).total_seconds()
    o7_words = ['o7', 'o/', '0/', 'o7']
    message_o7_words = [w.lower() for w in msg.content.split()]
    for o7_w in message_o7_words:
        if o7_w in o7_words and (key not in last_o7_time or diff >= 0):
            last_o7_time[key] = datetime.now() + timedelta(minutes=5)
            await msg.reply(o7_response(msg))


def o7_response(msg):
    o7_options = [f'o7 {msg.author}!', f'o7 {msg.author}! :) ', f' o777 {msg.author}!']
    return random.choice(o7_options)


# hellos and all - write different ones to cycle thru
last_hey_time = {}


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hey_time.get(key, datetime.now())).total_seconds()
    greet = ['hello', 'hola', 'hi', 'hii', 'hiii']
    message_greet = msg.content.split()[0].lower()
    parsed_message_greet = re.sub('[^A-Za-z0-9]+', '', message_greet)
    found_greet = parsed_message_greet in greet
    if (key not in last_hey_time or diff >= 0) and found_greet == True:
        last_hey_time[key] = datetime.now() + timedelta(minutes=5)
        await msg.reply(hello_response(msg))


def hello_response(msg):
    hello_options = [f'greetings dear {msg.author}! welcome welcome <3', f'hello {msg.author}! long time no see',
                     f'hey hey {msg.author}! hows life? ', f' hola amigo {msg.author}!']
    return random.choice(hello_options)


# crying
last_cry_time = {}


#@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_cry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_cry_time or diff >= 0) and ('cry') in msg.content.lower():
        last_cry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'WWWWAAAAAAHHHHHHHHHHHHHHHHH {msg.mention} is a crybaby')


# hungry
last_hungry_time = {}


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hungry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hungry_time or diff >= 0) and ('hungry') in msg.content.lower():
        last_hungry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'well why dont u eat something {msg.mention}?')


# hangry
last_hangry_time = {}


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hangry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hangry_time or diff >= 0) and ('hangry') in msg.content.lower():
        last_hangry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'well if u ate something {msg.mention} u would stop being agro...')


# brb
last_brb_time = {}


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_brb_time.get(key, datetime.now())).total_seconds()
    if (key not in last_brb_time or diff >= 0) and ('brb') in msg.content.lower():
        last_brb_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'ok {msg.mention} u will be missed dearly pls come back when u can we love u here')
