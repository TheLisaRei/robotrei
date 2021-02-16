from twitchbot import Command


# possibly change up
@Command('text', aliases=['reading'])
async def cmd_function(msg, *args):
    await msg.reply(
        'Consumer food stockpiling behavior and willingness to pay for food reserves in COVID-19 https://sci-hub.se/10.1007/s12571-020-01092-1 COVID-19 lockdown: implication for food security https://sci-hub.se/10.1007/s12571-020-01092-1')


@Command('topic', aliases=['lecture', 'lectures'])
async def cmd_function(msg, *args):
    await msg.reply('today I have food security in developing countries, economics&botany, rural development in developing areas')


@Command('today')
async def cmd_function(msg, *args):
    await msg.reply(
        'today I am attending my lectures on ms teams and reading research papers, also I am planning on doing some python stuff on stream in the evening, also thinking of getting a treadmill for under the desk, thoughts?')

@Command('exam')
async def cmd_function(msg, *args):
    await msg.reply('no exams coming up, thank the heavenss')

@Command('book')
async def cmd_function(msg, *args):
    await msg.reply(
        " In Never Mind, St. Aubyn renders this vivid tragedy with profound grace and precision, and introduces us to the unforgettable, complex figure of Patrick Melrose.  https://www.goodreads.com/book/show/13514899-never-mind")
