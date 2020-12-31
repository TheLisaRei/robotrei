from twitchbot import Command


@Command('commands', aliases=['command'], cooldown=300)
async def cmd_function(msg, *args):
    await msg.reply('feel free to try !robbery, !soulmate, !wisdom, !seduce, !karma, !vampire')


@Command('schedule')
async def cmd_function(msg, *args):
    await msg.reply(
        'weekdays: 9-ish till evening I study and have lectures, then python and/or eve online in the evenings till cca 10pm. weekends: surprise but basically a more chill study/python/eve time')


@Command('emotes', aliases=['emo','emoji'])
async def cmd_function(msg, *args):
    await msg.reply(' lisare1Hiss lisare1Skull lisare1Heart lisare1Robot lisare1Arson ')


@Command('subscribe', aliases=['sub'])
async def cmd_function(msg, *args):
    await msg.reply(' u get to use more than just these and also u will make me happy... lisare1Hiss lisare1Skull lisare1Heart lisare1Robot lisare1Arson ')
