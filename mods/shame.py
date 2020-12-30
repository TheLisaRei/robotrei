from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData, auto_register_mod
import random

# shame

is_shameful = set()


@Command('shame')
async def cmd_shame(msg: Message, *args):
    is_shameful.add(msg.author)
    await msg.reply(f'do you repent your sins? {msg.mention} [type yes/no]')


@auto_register_mod
class ShameMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in is_shameful:
            if 'yes' in msg.content.lower():
                await msg.reply(yes_options(msg))

            elif 'no' in msg.content.lower():
                await msg.reply(no_options(msg))

            is_shameful.discard(msg.author)


def yes_options(msg):
    yes_outcomes = [
        f'you have repented for your sins, but that means that you have accepted responsibility for them {msg.mention}... you have opened yourself to a lawsuit',
        f'its nice to meet a true child of god {msg.mention}... <3 bless u']
    return random.choice(yes_outcomes)


def no_options(msg):
    no_outcomes = [f'you are a dammed liar {msg.mention} and a sinner too',
                   f'unrepentant.. the devil lives inside you {msg.mention}... but i kinda like that, you have some coke btw?? i just *sniff sniff* need a pick me up']
    return random.choice(no_outcomes)
