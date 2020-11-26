from jsonhandler import FileIO
from twitchbot import Command, DummyCommand, SubCommand, CustomCommand
import json
import datetime


# data = json.load(open('customcommands.json', 'r'))


@Command('hi', aliases=['hello', 'hey'])
async def cmd_function(msg, *args):
    await msg.reply(f'hiiiii {msg.mention}')

@Command('github', aliases=['gb', 'git'])
async def cmd_function(msg, *args):
    await msg.reply('come bully me at https://github.com/lisareina/robotrei')


@Command('panic')
async def cmd_function(msg, *args):
    await msg.reply('AAAAAAAAAAAAAAAAAAAAAAA')

@Command('eve')
async def cmd_function(msg, *args):
    await msg.reply('send me ISK to "xymfa" and join w my link https://www.eveonline.com/signup?invc=046f680f-889d-4949-9a19-a383f98045e2')

@Command('time', aliases=['timezone'])
async def cmd_function(msg, *args):
    await msg.reply(
            f'time is  a social construct but here u go, it is: {(datetime.datetime.now()).strftime("%H:%M, %A %d/%m")}... gmt+1 babyy')

@Command('love')
async def cmd_function(msg, *args):
    await msg.reply(f'what is love {msg.mention}? do u love me? say !doyou')

cmd_doyou = DummyCommand('doyou')

@SubCommand(cmd_doyou, 'yes')
async def cmd_greet_yes(msg, *args):
    await msg.reply(f'awww thank uuuu but we should just be friendsss {msg.mention}!')


@SubCommand(cmd_doyou, 'no')
async def cmd_greet_no(msg, *args):
    await msg.reply(f'omggg i h8 u!!! banning u {msg.mention}!')

