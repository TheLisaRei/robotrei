from twitchbot import Command
from random import randint


# about Lisa

@Command('about', aliases=['lisa'])
async def cmd_function(msg, *args):
    await msg.reply('lisa is in her mid 20s doing an MScEng and learning python. she is from the cz :)')


@Command('age', aliases=['old'])
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a dog shed be dead... mid 20s')


@Command('height', aliases=['tall'])
async def cmd_function(msg, *args):
    await msg.reply('if lisa were a tree shed be 6ft, but as a human shes 185cm or so ')


@Command('where', aliases=['country', 'origin', 'from'])
async def cmd_function(msg, *args):
    await msg.reply('lisa is from the czech republic, central europe ')


@Command('languages', aliases=['lang'])
async def cmd_function(msg, *args):
    await msg.reply(
        'i speak czech, english, russian, spanish, and some french. also did 2 years of latin and a bit of trying to learn lojban and esperanto  ')


@Command('degree', aliases=['uni', 'university', 'study', 'student', 'major'])
async def cmd_function(msg, *args):
    await msg.reply('im doing an MScEng in agrieconomics ')


# technology
@Command('debian', aliases=['linux', 'distro', 'debian'])
async def cmd_function(msg, *args):
    await msg.reply('Debian GNU/Linux bullseye/sid')


@Command('equipment', aliases=['specs', 'pc', 'computer', 'laptop'])
async def cmd_function(msg, *args):
    await msg.reply(
        'no longer streaming from a laptop!! i am now on a desktop running Debian Linux. 2 monitors, 32inch and 23inch.')


@Command('monitor', aliases=['monitors', 'screen'])
async def cmd_function(msg, *args):
    await msg.reply('samsung uhd 32inch and the vertical is an old acer one that isnt sold anymore')


@Command('headphones', aliases=['earphones', 'jbl'])
async def cmd_function(msg, *args):
    await msg.reply(
        ' jbl live noise cancelling headphones. bluetooth. love them and they arent too expensive, currently waiting for pink ones w cat ears')


@Command('keyboard', aliases=['k', 'key'])
async def cmd_function(msg, *args):
    await msg.reply(
        'black/mint keyboard: filco minila air mx brown switches. pink/white keyboard: epomaker sk64 also brown switches ')


@Command('python', aliases=['p', 'ide'])
async def cmd_function(msg, *args):
    await msg.reply(
        'i am using pycharm. have been learning python since october 25th 2020, rn im working on this bot. use !pb to get the free python book u see me read on stream. ')


@Command('timer', aliases=['pomodoro', 'pomo'])
async def cmd_function(msg, *args):
    await msg.reply(
        'the timer is a pomodoro timer  you break your workday into 25-minute chunks separated by five-minute breaks. for productivity, you can start your own timer by doing !tomato and you will be tagged in chat when its time for a break')


@Command('iq')
async def cmd_function(msg, *args):
    random_iq = randint(70, 180)
    await msg.reply(f' so {msg.mention} ur IQ is {random_iq}...')


@Command('cat', aliases=['kitty'])
async def cmd_function(msg, *args):
    await msg.reply('the cat is a kappamon and reacts to stuff. very cool ')


@Command('pg', aliases=['pcguts'])
async def cmd_function(msg, *args):
    await msg.reply('PC Intel Core i9 9900 Coffee Lake 5 GHz, NVIDIA Quadro RTX 4000 8GB, RAM 64GB DDR4, SSD 3000 GB')
