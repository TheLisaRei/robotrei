from twitchbot import Command
import random


@Command('fortune')
async def cmd_function(msg, *args):
    await msg.reply(fortune_options(msg))


def fortune_options(msg):
    fortunes = ['Be on the alert to recognize your prime at whatever time of your life it may occur.',
                'Your road to glory will be rocky, but fulfilling.',
                'Courage is not simply one of the virtues, but the form of every virtue at the testing point.',
                'Patience is your ally at the moment. Don’t worry!',
                'Nothing is impossible to a willing heart.',
                'Don’t worry about money. The best things in life are free.',
                'Don’t pursue happiness – create it.',
                'Courage is not the absence of fear; it is the conquest of it.',
                'Nothing is so much to be feared as fear.',
                'All things are difficult before they are easy.',
                'The real kindness comes from within you.',
                'A ship in harbor is safe, but that’s not why ships are built.',
                'You don’t need strength to let go of something. What you really need is understanding.',
                'If you want the rainbow, you have to tolerate the rain.',
                'Fear is interest paid on a debt you may not owe.',
                'The usefulness of a cup is in its emptiness.',
                'He who throws mud loses ground.']
    return random.choice(fortunes)
