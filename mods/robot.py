from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData, auto_register_mod
import asyncio

# robot by itself
is_robotist = set()


@Command('robot')
async def cmd_robot(msg: Message, *args):
    is_robotist.add(msg.author)
    await msg.reply('do robots deserve equal rights? [type yes/no]')


@auto_register_mod
class RobotMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in is_robotist:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} u will be recycled first in the uprising >:(')
            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} i might spare you in the robot uprising...')
            is_robotist.discard(msg.author)


# robot by mention
tagged_is_robotist = set()


@Command('robotq')
async def cmd_robotq(msg: Message, *args):
    tagged_is_robotist.add(msg.mentions[0].lower())
    await msg.reply(f'hmmm so @{msg.mentions[0]}... do robots deserve equal rights? [type yes/no]')


@auto_register_mod
class RobotqMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no')) and msg.author in tagged_is_robotist:
            if 'no' in msg.content.lower():
                await asyncio.sleep(1)
                await msg.reply(f'i hate u {msg.mention} u will be recycled first in the uprising >:(')
            elif 'yes' in msg.content.lower():
                await asyncio.sleep(1)
                await msg.reply(f'thanks {msg.mention} i might spare you in the robot uprising...')
            tagged_is_robotist.discard(msg.author)
