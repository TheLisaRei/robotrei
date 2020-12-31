from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData, auto_register_mod, Command, \
    Message, custom_predicate, choice
import asyncio
import random


# all hail userman
@Command('robbery', aliases=['rob'])
async def cmd_function(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    victim = target.lstrip('@')
    print(msg.author)
    print(target)
    await msg.reply(
        f'{target}, gimme all ur money or get stabbed [type give/fight]')
    response = await msg.wait_for_reply(
        custom_predicate(

            lambda m: any(text in m.parts for text in ('give', 'fight')) and victim == m.author,
            msg=msg,
            same_author=False,
            same_channel=True,
        ), timeout=30
    )

    if not response.is_message:
        await msg.send_command(f'/me {target} didnt respond so RobotRei stabbed them to death with her trusty katana she bought at the mall. She tips her fedora to you and uses your money to move to Japan in hopes of finding true love... *flips trenchcoat wings*')
        return

    if 'give' in response.raw_value.parts:
        await msg.reply(f'thank you {target} for your generous donation. :)')
        await asyncio.sleep(5)
        await msg.send_command(
            f'/me (unfortunately {target} gets arrested for supporting the robot uprising shortly thereafter)')

    elif 'fight' in response.raw_value.parts:
        await msg.reply(choice([
            f'ohh {target} you are a brave soul... i will still stab u but w respect. a true warriors death.',
            f' uuu a karate master {target}, chop chop... u are a no match for a knife.. stab stab.. goodnight',
            f' hehe {target} u are overestimating ur abilities... ohh a KNIFE?? lord... would be trouble for me... if i didnt have this GUN... bang BANG byeeee',
            f' lol u troublemaker u {target}, u think u can take me on?? are u for real.... the disrespect... i think ill stab u particularly thoroughly, u will be fit to be the colander on a flying spaghetti monster believers head for their drivers license picture'

        ]))
        await msg.send_command(
            f'/me {target} is bleeding to death as RobotRei takes all their money anyway')
        await asyncio.sleep(5)
        await msg.reply(f'RIP {target} :(')
