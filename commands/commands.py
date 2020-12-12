from jsonhandler import FileIO
from twitchbot import Command, DummyCommand, SubCommand, CustomCommand
import json
import datetime


data = json.load(open('customcommands.json', 'r'))

# links
@Command('github', aliases=['gb', 'git'])
async def cmd_function(msg, *args):
    await msg.reply('come bully me at https://github.com/lisareina/robotrei')

@Command('eve', aliases=['e'])
async def cmd_function(msg, *args):
    await msg.reply('in game channel = LisaRei, ign = xymfa, and join w my link https://www.eveonline.com/signup?invc=046f680f-889d-4949-9a19-a383f98045e2 for one MILLION free skill points')

@Command('discord', aliases=['d'])
async def cmd_function(msg, *args):
    await msg.reply('come hang out on discord! https://discord.com/invite/YuXqUR6')

@Command('twitter', aliases=['t', 'bird'])
async def cmd_function(msg, *args):
    await msg.reply('follow me on twitter https://twitter.com/lisareistudy')

# basics

@Command('hi', aliases=['hello', 'hey'])
async def cmd_function(msg, *args):
    await msg.reply(f'hiiiii {msg.mention}')


@Command('panic')
async def cmd_function(msg, *args):
    await msg.reply('AAAAAAAAAAAAAAAAAAAAAAA')

@Command('bye')
async def cmd_function(msg, *args):
    await msg.reply(f'see u {msg.mention}, thnx for stopping by')

@Command('brb')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} will be back soon!!')

@Command('isk')
async def cmd_function(msg, *args):
    await msg.reply('send ISK to "xymfa" and i will not double it')


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

# practical
@Command('sound', aliases=['loud', 'quiet'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei something is wrong w the sound')

@Command('muted', aliases=['m', 'mic'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei u are muted')

# about
@Command('age')
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a dog shed be dead... mid 20s')

@Command('where', aliases=['country','origin', 'from'])
async def cmd_function(msg, *args):
    await msg.reply('lisa is from the czech republic, its a small country next to germany')




