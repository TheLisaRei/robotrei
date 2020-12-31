from twitchbot import Command

import datetime






# misc

@Command('me')
async def cmd_function(msg, *args):
    await msg.reply(f'you exist {msg.mention}')


@Command('tea')
async def cmd_function(msg, *args):
    await msg.reply('vanilla rooibos tea!')


@Command('amazon', aliases=['bezos', 'jeff'])
async def cmd_function(msg, *args):
    await msg.reply('amazon is a terrible company')


@Command('elon', aliases=['musk', 'muskrat'])
async def cmd_function(msg, *args):
    await msg.reply('elon musk should be made into a leather couch and left by the trashcan')


@Command('theend')
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(
            'thank u all for watching!!! pls follow me!!! also come to my discord and see u tomorrow!!! <3 https://discord.com/invite/YuXqUR6')


@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply(
        'weekdays: 9-ish till evening I study and have lectures, then python and/or eve online in the evenings till cca 10pm. weekends: surprise but basically a more chill study/python/eve time')


@Command('eve', aliases=['e', 'eveonline'])
async def cmd_function(msg, *args):
    await msg.reply(
        'Eve Online is a space-based, persistent world massively multiplayer online role-playing game developed and published by CCP Games. Players of Eve Online can participate in a number of in-game professions and activities, including mining, piracy, manufacturing, trading, exploration, and combat.')


# basics

@Command('panic')
async def cmd_function(msg, *args):
    await msg.reply('AAAAAAAAAAAAAAAAAAAAAAA')


@Command('indent', aliases=['indentation'])
async def cmd_function(msg, *args):
    await msg.reply('pssst @lisarei doesnt know how to indent pass it on')


@Command('mom')
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(
            'sorry guys this is my mom calling so i have to pick up so ill mute myself. shouldnt take toooo long.')


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
    await msg.reply(
        f'u gotta use channel points to make me not sit like a pretzel... but just this once ill sit up straight anyway')


@Command('hydrate')
async def cmd_function(msg, *args):
    await msg.reply(
        f'u gotta use channel points to make me drinkkk... but just this once ill take a sip since its u {msg.mention}')


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
    await msg.reply(f'u have been hugged @{msg.mentions[0]} lisare1Heart ')


@Command('thankyou', aliases=['thnx', 'ty'])
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f' oooo @{msg.mentions[0]} thank u!!! <3 i love u')


@Command('streamershoutout', aliases=['streamer', 'ss'])
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'shoutout to @{msg.mentions[0]} who is also a streamer!! go follow them')


# about

@Command('games', aliases=['game'])
async def cmd_function(msg, *args):
    await msg.reply('stardew valley, eve online and some minecraft... if u wanna play w me go to my discord')


@Command('stardew')
async def cmd_function(msg, *args):
    await msg.reply(
        'Stardew Valley is an open-ended country-life RPG! Youve inherited your grandfathers old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.')


# bot feedbackdatabase
@Command('goodbot', aliases=['goodrobot', 'good'])
async def cmd_function(msg, *args):
    await msg.reply(f'awww thank u {msg.mention} i am glad u like me')


@Command('badbot', aliases=['badrobot', 'bad'])
async def cmd_function(msg, *args):
    await msg.reply(f'wow..... {msg.mention} i have feelings too you know... u try being a bot.... its not so easy')
    # it would add a point or something????? into the database


@Command('bot')
async def cmd_function(msg, *args):
    await msg.reply(
        'i am not a bot i am a robot.... use !robot pls. but fine fine... i am a twitchbot, made in python, to see my insides use !github')


@Command('sorry')
async def cmd_function(msg, *args):
    await msg.reply(f'hmmm i dont know if i forgive you... robots never forgive or forget')


@Command('die')
async def cmd_function(msg, *args):
    await msg.reply('oh wow... u big meanie.... speechlesssss')


@Command('daddy', aliases=['framework', 'twitchbot'])
async def cmd_function(msg, *args):
    await msg.reply(f'my daddy is https://github.com/sharkbound/PythonTwitchBotFramework')


@Command('say')
async def cmd_say(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(' '.join(args))
