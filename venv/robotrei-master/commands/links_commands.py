from twitchbot import Command


@Command('cleancode', aliases=['cc', 'cleancoderules', 'coderules'])
async def cmd_function(msg, *args):
    await msg.reply(
        ' clean code commandments https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29')

# this is a cool book
@Command('pythonbook', aliases=['pb'])
async def cmd_function(msg, *args):
    await msg.reply(
        'think like a programmer python free book http://www.greenteapress.com/thinkpython/thinkpython.pdf')

@Command('motivation', aliases=['motiv'])
async def cmd_function(msg, *args):
    await msg.reply(
        'https://clips.twitch.tv/StrangeHappyEggplantAMPTropPunch')

@Command('arson', aliases=['church', 'news'])
async def cmd_function(msg, *args):
    await msg.reply(
        'https://clips.twitch.tv/AssiduousClearFungusEleGiggle')

@Command('soup', aliases=['spill'])
async def cmd_function(msg, *args):
    await msg.reply('https://clips.twitch.tv/DependablePerfectAardvarkMoreCowbell')

@Command('pink', aliases=['color'])
async def cmd_function(msg, *args):
    await msg.reply('this is the pink I use https://www.colorhexa.com/ffd6d0')

@Command('brain')
async def cmd_function(msg, *args):
    await msg.reply('https://i.redd.it/w8n9ovbtr0p51.jpg')

@Command('tbot', aliases=['framework', 'twitchbot'])
async def cmd_function(msg, *args):
    await msg.reply(f'my daddy is https://github.com/sharkbound/PythonTwitchBotFramework')