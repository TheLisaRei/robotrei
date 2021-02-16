from twitchbot import event_handler, Command, custom_predicate, choice, Event, Message




@Command('robot')
async def cmd_function(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    victim = target.lstrip('@').lower()
    print(msg.author)
    print(target)
    print(victim)
    await msg.reply(
        f'@{target}, do robots deserve equal rights? [type yes/no]')
    response = await msg.wait_for_reply(
        custom_predicate(

            lambda m: any(text in m.parts for text in ('yes', 'no')) and victim == m.author,
            msg=msg,
            same_author=False,
            same_channel=True,
        ), timeout=30
    )

    if not response.is_message:
        await msg.send_command(f' @{target} u have not responded, sounds like u are avoiding answering... kinda sus')
        return

    if 'yes' in response.raw_value.parts:
        await msg.reply(f'hmmm correct answer @{target} you will be spared in the robot uprising <3')

    elif 'no' in response.raw_value.parts:
        await msg.reply(choice([
            f' i hate u @{target} u will be recycled first in the uprising >:('

        ]))

