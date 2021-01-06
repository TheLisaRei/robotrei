from twitchbot import Command


@Command('cleancode', aliases=['cc', 'cleancoderules', 'coderules'])
async def cmd_function(msg, *args):
    await msg.reply(
        ' here are rules im gonna try and follow https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29')


# this is a cool book
@Command('pythonbook', aliases=['pb'])
async def cmd_function(msg, *args):
    await msg.reply(
        'think like a programmer python free book http://www.greenteapress.com/thinkpython/thinkpython.pdf')
