from twitchbot import BaseBot, load_commands_from_directory
from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData
from datetime import datetime, timedelta

# works
@event_handler(Event.on_user_join)
async def on_user_join(user: str, channel: Channel):
    print(f'{user} joined')
    # await channel.send_message(f'hi @{user}')

@event_handler(Event.on_user_part)
async def on_user_part(user: str, channel: Channel):
    print(f'{user} left')

# dont know if it works but it should?
@event_handler(Event.on_channel_subscription)
async def on_channel_subscription(subscriber: str, channel: Channel, msg: Message):
    await channel.send_message(f'omg @{subscriber} just subscribed wooowww thank uuu')


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    if 'Thank you for following' in msg.content:
        await msg.reply('yes yes thank u for following! <3 i am the bot of this channel, my name is RobotRei')

@event_handler(Event.on_bits_donated)
async def on_bits_donated(self, msg: Message, bits: int):
    await msg.reply('thank you for cheering')



# initialize the variable
lastCandyTime = datetime.now()


@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    if 'candy' in msg.content:
        global lastCandyTime

        currentTime = datetime.now()
        allowedTime = lastCandyTime + timedelta(seconds=600)
        # compare the candyTime variable to current timestamp
        print(currentTime)
        print(allowedTime)
        print(currentTime > allowedTime)
        print(currentTime < allowedTime)
        if currentTime > allowedTime:
            lastCandyTime = currentTime
            await msg.reply('i would like some candy...')

lastCookiesTime = datetime.now()



last_hello_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hello_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hello_time or diff >= 0) and 'hello' in msg.content.lower():
        last_hello_time[key] = datetime.now() + timedelta(minutes=5)
        await msg.reply(f'hello {msg.author}!')



if __name__ == '__main__':
    load_commands_from_directory('./commands')
    BaseBot().run()
