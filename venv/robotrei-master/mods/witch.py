from twitchbot import Command, Message, custom_predicate, choice


@Command('wiseman')
async def cmd_wiseman(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    print(target)
    await msg.reply(
        f'{target}, you walk up to a wise looking man. he asks if you want to walk to his [type left/right]')
    response = await msg.wait_for_reply(
        custom_predicate(

            lambda m: any(text in m.parts for text in ('left', 'right')) and target == f'@{m.author}',
            msg=msg,
            same_author=False,
            same_channel=True,
        ), timeout=30
    )

    if not response.is_message:
        await msg.reply('the wise man got impatient and smacked you with his hand, it kills you instantly...')
        return

    if 'left' in response.raw_value.parts:
        await msg.reply(f'{target}, you walk to the left of the wise man, ' + choice([
            'he promptly slaps you, seems you choose wrong',
            'you walk past him and into a hole covered by a rug, idk why a rug is covering a hole on the road, but it was...'
        ]))
    elif 'right' in response.raw_value.parts:
        await msg.reply(f'{target}, you walk to the right of the wise man, ' + choice([
            'you run right into a canvas, the wise man disappears, and the sky falls down on you, killing you instantly...',
            'the walk is pleasant, you enjoy it very much!'
        ]))
