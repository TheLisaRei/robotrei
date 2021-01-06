from twitch import Command, Message
from random import randint

@Command('iq')
async def cmd_function(msg: Message, *args):
    random_iq = randint(70, 180)
    await msg.reply(f'Here is a random IQ for you! {random_iq}')
