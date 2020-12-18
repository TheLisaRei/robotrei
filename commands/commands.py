from jsonhandler import FileIO
from twitchbot import Command, DummyCommand, SubCommand, CustomCommand
from twitchbot import auto_register_mod
import json
import datetime


# data = json.load(open('customcommands.json', 'r'))
# print(data)

# change each stream
@Command('text', aliases=['reading'])
async def cmd_function(msg, *args):
    await msg.reply('currently i am writing about water management policies, the aral sea disaster and the role of women in water management in central asia')

@Command('song', aliases=['music'])
async def cmd_function(msg, *args):
    await msg.reply('currently playing this: https://www.youtube.com/watch?v=OVPPOwMpSpQ')

@Command('today')
async def cmd_function(msg, *args):
    await msg.reply('today i am writing my essay, more about that under !text. also im eating breakfast and then gonna be playing eve')

@Command('tea')
async def cmd_function(msg, *args):
    await msg.reply('vanilla rooibos tea!')

@Command('amazon')
async def cmd_function(msg, *args):
    await msg.reply('amazon is a terrible company')

@Command('theend')
async def cmd_function(msg, *args):
    await msg.reply('thank u all for watching!!! pls follow me!!! also come to my discord and see u tomorrow!!! <3 https://discord.com/invite/YuXqUR6')

@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply('weekdays: 9-ish till evening I study and have lectures, then python and/or eve online in the evenings till cca 10pm. weekends: surprise but basically a more chill study/python/eve time')

# links
@Command('github', aliases=['gb', 'git'])
async def cmd_function(msg, *args):
    await msg.reply('come bully me at https://github.com/lisareina/robotrei')

@Command('invite')
async def cmd_function(msg, *args):
    await msg.reply('in game channel = LisaRei, ign = xymfa, and join w my link https://www.eveonline.com/signup?invc=046f680f-889d-4949-9a19-a383f98045e2 for one MILLION free skill points')

@Command('eve', aliases=['e', 'eveonline'])
async def cmd_function(msg, *args):
    await msg.reply('Eve Online is a space-based, persistent world massively multiplayer online role-playing game developed and published by CCP Games. Players of Eve Online can participate in a number of in-game professions and activities, including mining, piracy, manufacturing, trading, exploration, and combat.')

@Command('discord', aliases=['d'])
async def cmd_function(msg, *args):
    await msg.reply('come hang out on discord! https://discord.com/invite/YuXqUR6 or use !dw to whisper the link to urself')

@Command('twitter', aliases=['t', 'bird'])
async def cmd_function(msg, *args):
    await msg.reply('follow me on twitter https://twitter.com/lisareistudy')

@Command('instagram', aliases=['i', 'insta', 'ig'])
async def cmd_function(msg, *args):
    await msg.reply('my insta is: https://www.instagram.com/thelisarei/')

# basics

@Command('panic')
async def cmd_function(msg, *args):
    await msg.reply('AAAAAAAAAAAAAAAAAAAAAAA')

@Command('mom')
async def cmd_function(msg, *args):
    await msg.reply('sorry guys this is my mom calling so i have to pick up so ill mute myself. shouldnt take toooo long.')


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

# practical
@Command('sound', aliases=['loud', 'quiet'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei something is wrong w the sound')

@Command('muted', aliases=['m', 'mic'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei u are muted')

@Command('posture')
async def cmd_function(msg, *args):
    await msg.reply(f'u gotta use channel points to make me not sit like a pretzel... but just this once ill sit up straight anyway')

@Command('hydrate')
async def cmd_function(msg, *args):
    await msg.reply(f'u gotta use channel points to make me drinkkk... but just this once ill take a sip since its u {msg.mention}')

@Command('situpstraightsis')
async def cmd_function(msg, *args):
    allowed_users = {'i_thanvanth'}
    if msg.author in allowed_users:
        await msg.reply('T says sit up @lisarei')

@Command('lurk')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} is gonna be lurking <3')

@Command('hug')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u have been hugged @{msg.mentions[0]}')


# about
@Command('age')
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a dog shed be dead... mid 20s')

@Command('height', aliases=['tall'])
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a tree shed be 6ft, but as a human shes 185cm or so')

@Command('where', aliases=['country','origin', 'from'])
async def cmd_function(msg, *args):
    await msg.reply('lisa is from the czech republic, its a small country next to germany')

@Command('python')
async def cmd_function(msg, *args):
    await msg.reply('i am using pycharm pro, have been learning since october 2020, rn im working on this bot')

@Command('equipment', aliases=['specs'])
async def cmd_function(msg, *args):
    await msg.reply('macbook pro 2015, keyboard: filco minila air mx brown switches')

@Command('keyboard')
async def cmd_function(msg, *args):
    await msg.reply('keyboard: filco minila air mx brown switches')

@Command('languages')
async def cmd_function(msg, *args):
    await msg.reply('i speak czech, english, russian, spanish, and some french. also did 2 years of latin and a bit of trying to learn lojban and esperanto')

@Command('games', aliases=['game'])
async def cmd_function(msg, *args):
    await msg.reply('stardew valley, eve online and some minecraft... if u wanna play w me go to my discord')

@Command('stardew')
async def cmd_function(msg, *args):
    await msg.reply('Stardew Valley is an open-ended country-life RPG! Youve inherited your grandfathers old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.')

@Command('degree')
async def cmd_function(msg, *args):
    await msg.reply('im doing an MScEng in agricultural economics and international development')

# bot feedback
@Command('goodbot', aliases=['goodrobot', 'good'])
async def cmd_function(msg, *args):
    await msg.reply(f'awww thank u {msg.mention} i am glad u like me')

@Command('badbot', aliases=['badrobot', 'bad'])
async def cmd_function(msg, *args):
    await msg.reply(f'wow..... {msg.mention} i have feelings too you know... u try being a bot.... its not so easy')

@Command('bot')
async def cmd_function(msg, *args):
    await msg.reply('i am not a bot i am a robot.... use !robot pls. but fine fine... i am a twitchbot, made in python, to see my insides use !github')

@Command('sorry')
async def cmd_function(msg, *args):
    await msg.reply(f'hmmm i dont know if i forgive you... robots never forgive or forget')

@Command('die')
async def cmd_function(msg, *args):
    await msg.reply('oh wow... u big meanie.... speechlesssss')

@Command('daddy')
async def cmd_function(msg, *args):
    await msg.reply(f'my daddy is https://github.com/sharkbound/PythonTwitchBotFramework but who is your daddy??? {msg.mention}')

@Command('say')
async def cmd_say(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(' '.join(args))