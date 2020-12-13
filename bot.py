from twitchbot import BaseBot, load_commands_from_directory
from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData,  auto_register_mod
from datetime import datetime, timedelta

# love
sent_love = set()


@Command('love')
async def cmd_love(msg: Message, *args):
    sent_love.add(msg.author)
    await msg.reply('do you love me? [type yes/no]')


@auto_register_mod
class LoveMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in sent_love:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} i will remember this... >:(')
            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} but we should just be friends')
            sent_love.discard(msg.author)

# robot
is_robotist = set()

@Command('robot')
async def cmd_robot(msg: Message, *args):
    is_robotist.add(msg.author)
    await msg.reply('do robots deserve equal rights? [type yes/no]')


@auto_register_mod
class RobotMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in is_robotist:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} u will be recycled first in the uprising >:(')
            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} i might spare you in the robot uprising...')
            is_robotist.discard(msg.author)

#
is_robotist = set()

@Command('robot')
async def cmd_robot(msg: Message, *args):
    is_robotist.add(msg.author)
    await msg.reply('do robots deserve equal rights? [type yes/no]')


@auto_register_mod
class RobotMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in is_robotist:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} u will be recycled first in the uprising >:(')
            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} i might spare you in the robot uprising...')
            is_robotist.discard(msg.author)

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


last_hello_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hello_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hello_time or diff >= 0) and 'hello' in msg.content.lower():
        last_hello_time[key] = datetime.now() + timedelta(minutes=5)
        await msg.reply(f'hello {msg.author}!')


last_cry_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_cry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_cry_time or diff >= 0) and ('cry') in msg.content.lower():
        last_cry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'WWWWAAAAAAHHHHHHHHHHHHHHHHH {msg.mention} is a crybaby')


last_hungry_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hungry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hungry_time or diff >= 0) and ('hungry') in msg.content.lower():
        last_hungry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'well why dont u eat something {msg.mention}?')

last_hangry_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_hangry_time.get(key, datetime.now())).total_seconds()
    if (key not in last_hangry_time or diff >= 0) and ('hangry') in msg.content.lower():
        last_hangry_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'well if u ate something {msg.mention} u would stop being agro...')


last_brb_time = {}
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    key = (msg.author, msg.channel_name)
    diff = (datetime.now() - last_brb_time.get(key, datetime.now())).total_seconds()
    if (key not in last_brb_time or diff >= 0) and ('brb') in msg.content.lower():
        last_brb_time[key] = datetime.now() + timedelta(minutes=2)
        await msg.reply(f'ok {msg.mention} u will be missed dearly pls come back when u can we love u here')
if __name__ == '__main__':
    load_commands_from_directory('./commands')
    BaseBot().run()
