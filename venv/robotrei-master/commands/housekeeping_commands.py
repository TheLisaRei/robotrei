from twitchbot import Command


@Command('commands', aliases=['command'])
async def cmd_function(msg, *args):
    await msg.reply(' feel free to try !robbery, !soulmate, !wisdom, !seduce, !karma, !vampire, !zoo ')


@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply(
        'weekdays: 9-ish till evening I study and have lectures, then python and/or eve online in the evenings till cca 10pm. weekends: surprise but basically a more chill study/python/eve time ')


@Command('treat')
async def cmd_function(msg, *args):
    await msg.reply(
        'hey @lisarei i think ur baby needs a treat')

@Command('dog')
async def cmd_function(msg, *args):
    await msg.reply(
        'doggos name is prince and hes a black pointer')




@Command('theend')
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(
            'thank u all for watching!!! pls follow me!!! also come to my discord and see u tomorrow!!! <3 https://discord.com/invite/YuXqUR6 ')


@Command('mom', aliases=['call'])
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(
            'sorry guys this is my mom/someone calling so i have to pick up so ill mute myself. shouldnt take toooo long.')

@Command('brb')
async def cmd_function(msg, *args):
    await msg.reply(f'{msg.mention} will be back soon!!')


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

@Command('thankyou', aliases=['thnx', 'ty'])
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f' oooo @{msg.mentions[0]} thank u!!! <3 i love u')


@Command('streamershoutout', aliases=['streamer', 'ss'])
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(f'shoutout to @{msg.mentions[0]} who is also a streamer!! go follow them!! twitch.com/{msg.mentions[0]}')

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
