from twitchbot import Command


@Command('commands', aliases=['command'])
async def cmd_function(msg, *args):
    await msg.reply(' lisare1Heart  feel free to try !robbery, !soulmate, !wisdom, !seduce, !karma, !vampire, !zoo lisare1Heart ')


@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply(
        'lisare1Heart weekdays: 9-ish till evening I study and have lectures, then python and/or eve online in the evenings till cca 10pm. weekends: surprise but basically a more chill study/python/eve time lisare1Heart ')


@Command('emotes', aliases=['emo','emoji'])
async def cmd_function(msg, *args):
    await msg.reply(' lisare1Hiss lisare1Skull lisare1Heart lisare1Robot lisare1Arson ')


@Command('subscribe', aliases=['sub'])
async def cmd_function(msg, *args):
    await msg.reply(' u get to use more than just these and also u will make me happy... lisare1Hiss lisare1Skull lisare1Heart lisare1Robot lisare1Arson ')

@Command('theend')
async def cmd_function(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(
            'lisare1Heart  thank u all for watching!!! pls follow me!!! also come to my discord and see u tomorrow!!! <3 https://discord.com/invite/YuXqUR6 lisare1Heart ')


