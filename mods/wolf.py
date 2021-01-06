from twitchbot import *

# strip punctuation and add a random choice

def create_text_choice_command(name: str, initial_message: str, **responses: list):
    @Command(name, prefix='!')
    async def choice_command(msg: Message, *args):
        user = msg.arg_or_default(0, msg.author).lstrip('@')
        await msg.reply(initial_message)

        resp = await msg.wait_for_reply(
            custom_predicate(lambda m: m.author == user and m.parts[0].lower().strip('!') in responses, msg=msg, same_author=False),
            timeout=20
        )

        if resp.is_message:
            await msg.reply(choice(responses[resp.raw_value.parts[0].lower().strip('!')]).format(user=user))
        else:
            await msg.reply('it seems it timed out...')

    return choice_command


create_text_choice_command('shop', ' you walk into a weapons shop, you can purchase these items: sword, axe, wolf',
                           sword=['@{user} you pick up the sword, but grabbed the pointy end...'],
                           axe=['@{user} you grab the axe and attack the wall, the place comes falling down, as well as you...'],
                           wolf=['@{user} you grab the wolf, WAIT, why is there a live wolf in the shop?!?!'])

create_text_choice_command('zoo', ' you walk into a zoo and you see: (choose one: zebra, lion, hippo, crocodile, panda)',
                           zebra=['@{user} you see a herd of zebras and they all stare at you while chewing. reminds you of cows you used to see at grandmas farm', 'you cant find the zebra enclosure... why are all the signs so confusing?? ugh @{user}'],
                           lion=['@{user} you go towards the lion exhibit and turns out its feeding time, kinda gross but also kinda cool. huh'],
                           hippo=['@{user} did u know that hippos are one of the deadliest animals??? very fast chonky boys with big mouths'],
                           crocodile=['@{user} you go to the crocodile pond and try to find one, but it seems like they are all underwater, maybe come back later'],
                           panda=['@{user} you go take a look at the pandas, you are in luck because a big fluffy panda is sitting right by the glass and chewing on some bamboo. you make eye contact. amazing. you stand there for about 15 min and then go get some donuts from the stand next to the flamingos'])
