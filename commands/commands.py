from twitchbot import Command, Message
import asyncio
import datetime



# start pomodoro timer
@Command('tomato')
async def cmd_function(msg, *args):
    await msg.reply(f'ok {msg.mention} you should work/study for the next 25min, ill notify u when its time for a break')
    await asyncio.sleep(1500)
    await msg.reply(f' {msg.mention} congrats, your work time has finished, enjoy a 5min break, ill tell you when its over')
    await asyncio.sleep(300)
    await msg.reply(f' {msg.mention} congrats, you completed a cycle, use !tomato to start again')


# misc

@Command('me')
async def cmd_function(msg, *args):
    await msg.reply(f'you exist {msg.mention}')

@Command('coffee')
async def cmd_function(msg, *args):
    await msg.reply(f'lol u wish {msg.mention}... i am not ur secretary lisare1Robot  go make ur own coffee u lazy kiddo')

@Command('book')
async def cmd_function(msg, *args):
    await msg.reply('liveblog by megan boyle.. LIVEBLOG is an historical text, extremely unique and shockingly human. In 2013, Megan Boyle was unhappy with the life she was living and wanted to document it on the internet for an audience.  https://www.amazon.com/LIVEBLOG-Megan-Boyle/dp/099921862X')

@Command('tea')
async def cmd_function(msg, *args):
    await msg.reply('vanilla rooibos tea!')

@Command('brain')
async def cmd_function(msg, *args):
    await msg.reply('https://i.redd.it/w8n9ovbtr0p51.jpg')

@Command('amazon', aliases=['bezos', 'jeff'])
async def cmd_function(msg, *args):
    await msg.reply('amazon is a terrible company')


@Command('elon', aliases=['musk', 'muskrat'])
async def cmd_function(msg, *args):
    await msg.reply('elon musk should be made into a leather couch and left by the trashcan')



@Command('eve', aliases=['e', 'eveonline'])
async def cmd_function(msg, *args):
    await msg.reply(
        'Eve Online is a space-based, persistent world massively multiplayer online role-playing game developed and published by CCP Games. Players of Eve Online can participate in a number of in-game professions and activities, including mining, piracy, manufacturing, trading, exploration, and combat.')


# basics


@Command('upset', aliases=['angry'])
async def cmd_function(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    print(target)
    await msg.reply(f'{target} is upset :( what did u all do? angry!? unacceptable... terrible!!' )


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


@Command('brb')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} will be back soon!!')


@Command('isk')
async def cmd_function(msg, *args):
    await msg.reply('send ISK to "xymfa" and i will not double it')


@Command('time', aliases=['timezone'])
async def cmd_function(msg, *args):
    await msg.reply(
        f'time is  a social construct but here u go, it is: {(datetime.datetime.now()).strftime("%H:%M:%S, %A %d/%m")}... gmt+1 babyy')


# practical
@Command('sound', aliases=['loud', 'quiet', 'volume'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei something is wrong w the sound')


@Command('muted', aliases=['m', 'mic'])
async def cmd_function(msg, *args):
    await msg.reply(f'@lisarei u are muted')


@Command('posture')
async def cmd_function(msg, *args):
    await msg.reply(
        f'u gotta use channel points to make me not sit like a pretzel... but just this once ill sit up straight anyway')


@Command('hydrate', aliases=['drink', 'water'])
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


@Command('sticker', aliases=['smiley', 'smileyface', 'smile', 'stick'], cooldown=60)
async def cmd_function(msg, *args):
    await msg.reply('eyyy @lisarei i want u to stick a smiley face somewhere')

@Command('hug')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u have been hugged @{msg.mentions[0]} lisare1Heart ')


@Command('poke')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u have been poked @{msg.mentions[0]} lisare1Heart ')


@Command('kiss')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'ugh u have been kissed @{msg.mentions[0]}... ew. unsanitary.. its covid season this is not allowed.')

@Command('kill')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'lol u have been killed @{msg.mentions[0]}... rip i guess heh')

@Command('resurrect')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'ooo u have been brought back from the dead @{msg.mentions[0]}... freaky lol')

@Command('bully')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u suck and cant sit with us @{msg.mentions[0]}... >:( ')

@Command('thankyou', aliases=['thnx', 'ty'])
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f' oooo @{msg.mentions[0]} thank u!!! <3 i love u')


@Command('streamershoutout', aliases=['streamer', 'ss'])
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
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
