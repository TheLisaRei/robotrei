from twitchbot import Command


# possibly change up
@Command('text', aliases=['reading'])
async def cmd_function(msg, *args):
    await msg.reply('today im just messing around w the bot and vibing')


@Command('today')
async def cmd_function(msg, *args):
    await msg.reply('today im just messing around w the bot and vibing, studying')
