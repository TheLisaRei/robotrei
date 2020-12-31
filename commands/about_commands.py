from twitchbot import Command

# about Lisa
@Command('age')
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a dog shed be dead... mid 20s lisare1Arson')


@Command('height', aliases=['tall'])
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a tree shed be 6ft, but as a human shes 185cm or so lisare1Arson ')


@Command('where', aliases=['country', 'origin', 'from'])
async def cmd_function(msg, *args):
    await msg.reply('lisa is from the czech republic, germany is the country next to CZ lisare1Skull ')

@Command('languages', aliases=['lang'])
async def cmd_function(msg, *args):
    await msg.reply(
        'i speak czech, english, russian, spanish, and some french. lisare1Arson  also did 2 years of latin and a bit of trying to learn lojban and esperanto')


@Command('degree', aliases=['uni', 'university', 'study', 'student'])
async def cmd_function(msg, *args):
    await msg.reply('im doing an MScEng in agricultural economics and international development lisare1Arson ')


# technology
@Command('equipment', aliases=['specs','pc', 'computer'])
async def cmd_function(msg, *args):
    await msg.reply('macbook pro 2015, keyboard: filco minila air mx brown switches lisare1Robot ')


@Command('keyboard', aliases=['k', 'key'])
async def cmd_function(msg, *args):
    await msg.reply('keyboard: filco minila air mx brown switches lisare1Robot')


@Command('python', aliases=['p', 'ide'])
async def cmd_function(msg, *args):
    await msg.reply('i am using pycharm pro lisare1Hiss  have been learning since october 25th 2020, rn im working on this bot lisare1Robot')

@Command('timer', aliases=['pomodoro', 'tomato'])
async def cmd_function(msg, *args):
    await msg.reply('the timer is a pomodoro timer lisare1Heart  you break your workday into 25-minute chunks separated by five-minute breaks. for productivity lisare1Robot')
