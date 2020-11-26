from jsonhandler import FileIO
from twitchbot import Command
import datetime

@Command('hi')
async def cmd_function(msg, *args):
    await msg.reply(f'i was called! {msg.mention}')

@Command('time')
async def cmd_function(msg, *args):
    await msg.reply(
            f'time is  a social construct but here u go, it is: {(datetime.datetime.now()).strftime("%H:%M, %A %d/%m")}... gmt+1 babyy')

