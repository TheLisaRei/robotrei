from twitchbot import Command


@Command('commands', aliases=['command'], cooldown=300)
async def cmd_function(msg, *args):
    await msg.reply('feel free to try !robbery, !soulmate, !wisdom')


@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply(
        'weekdays: 9-ish till evening I study and have lectures, then python and/or eve online in the evenings till cca 10pm. weekends: surprise but basically a more chill study/python/eve time')
