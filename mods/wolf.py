from twitchbot import *

# strip punctuation and add a random choice

def create_text_choice_command(name: str, initial_message: str, **responses: list):
    @Command(name, prefix='!')
    async def choice_command(msg: Message, *args):
        user = msg.arg_or_default(0, msg.author).lstrip('@')
        await msg.reply(initial_message)

        resp = await msg.wait_for_reply(
            custom_predicate(lambda m: m.author == user and m.parts[0].lower().lstrip('!') in responses, msg=msg, same_author=False),
            timeout=20
        )

        if resp.is_message:
            await msg.reply(choice(responses[resp.raw_value.parts[0].lower().lstrip('!')]).format(user=user))
        else:
            await msg.reply('it seems it timed out...')

    return choice_command


create_text_choice_command('shop', 'you walk into a weapons shop, you can purchase these items: sword, axe, wolf',
                           sword=['@{user} you pick up the sword, but grabbed the pointy end...'],
                           axe=['@{user} you grab the axe and attack the wall, the place comes falling down, as well as you...'],
                           wolf=['@{user} you grab the wolf, WAIT, why is there a live wolf in the shop?!?!'])

