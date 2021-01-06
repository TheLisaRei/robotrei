from twitchbot import Command
from random import randint
# about Lisa

@Command('about', aliases=['lisa'])
async def cmd_function(msg, *args):
    await msg.reply(' lisare1Heart  lisa is in her mid 20s doing an msceng and learning python. she is from the cz :) lisare1Heart ')

@Command('age')
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a dog shed be dead... mid 20s lisare1Arson')


@Command('height', aliases=['tall'])
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a tree shed be 6ft, but as a human shes 185cm or so lisare1Arson ')

@Command('headphones', aliases=['earphones', 'jbl'])
async def cmd_function(msg, *args):
    await msg.reply(' jbl live noise cancelling headphones. bluetooth. love them and they arent too expensive lisare1Arson ')

@Command('where', aliases=['country', 'origin', 'from'])
async def cmd_function(msg, *args):
    await msg.reply('lisa is from the czech republic, central europe lisare1Skull ')

@Command('languages', aliases=['lang'])
async def cmd_function(msg, *args):
    await msg.reply(
        'i speak czech, english, russian, spanish, and some french. lisare1Arson  also did 2 years of latin and a bit of trying to learn lojban and esperanto lisare1Heart ')


@Command('degree', aliases=['uni', 'university', 'study', 'student'])
async def cmd_function(msg, *args):
    await msg.reply('im doing an MScEng in agricultural economics and international development lisare1Arson ')


# technology
@Command('equipment', aliases=['specs','pc', 'computer', 'laptop'])
async def cmd_function(msg, *args):
    await msg.reply('macbook pro 2015, keyboard: filco minila air mx brown switches lisare1Robot ')


@Command('keyboard', aliases=['k', 'key'])
async def cmd_function(msg, *args):
    await msg.reply('lisare1Heart  keyboard: filco minila air mx brown switches lisare1Robot')


@Command('python', aliases=['p', 'ide'])
async def cmd_function(msg, *args):
    await msg.reply('i am using pycharm pro lisare1Hiss  have been learning since october 25th 2020, rn im working on this bot lisare1Robot')

@Command('timer', aliases=['pomodoro'])
async def cmd_function(msg, *args):
    await msg.reply('lisare1Heart  the timer is a pomodoro timer lisare1Heart  you break your workday into 25-minute chunks separated by five-minute breaks. for productivity lisare1Robot')

@Command('iq')
async def cmd_function(msg, *args):
    random_iq = randint(70, 180)
    await msg.reply(f' so {msg.mention} ur IQ is {random_iq}...')


@Command('follow', aliases=['ff'])
async def cmd_function(msg, *args):
    await msg.reply('yall pls follow this channel it helps a lot lisare1Heart  ')


@Command('cat', aliases=['kitty'])
async def cmd_function(msg, *args):
    await msg.reply('the cat is a kappamon and reacts to stuff. very cool lisare1Robot')


@Command('soup', aliases=['spill'])
async def cmd_function(msg, *args):
    await msg.reply('https://clips.twitch.tv/DependablePerfectAardvarkMoreCowbell')