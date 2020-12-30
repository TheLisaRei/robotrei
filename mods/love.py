from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData, auto_register_mod


# love by itself
is_lover = set()


@Command('love')
async def cmd_lover(msg: Message, *args):
    is_lover.add(msg.author)
    await msg.reply('do you love me? [type yes/no/maybe]')


@auto_register_mod
class LoveMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no', 'maybe')) and msg.author in is_lover:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} i will remember this... >:(')
            elif 'maybe' in msg.content.lower():
                await msg.reply(f'how can u not know {msg.mention} >:(')

            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} but we should just be friends')
            is_lover.discard(msg.author)


# love by mention
tagged_is_lover = set()


@Command('taglove')
async def cmd_love(msg: Message, *args):
    if len(msg.mentions) == 0:
        await msg.reply(f' u gotta tag someone {msg.author}!! its called !taglove for a reason')
        return
    tagged_is_lover.add(msg.mentions[0].lower())
    await msg.reply(f'hey @{msg.mentions[0]} i have a question... ummm... do you love me? [type yes/no/maybe]')


@auto_register_mod
class TagloveMod(Mod):
    async def on_privmsg_received(self, msg: Message):
        if any(word in msg.content.lower() for word in ('yes', 'no', 'maybe')) and msg.author in tagged_is_lover:
            if 'no' in msg.content.lower():
                await msg.reply(f'i hate u {msg.mention} i will remember this... >:(')
            elif 'maybe' in msg.content.lower():
                await msg.reply(f'how can u not know {msg.mention} >:( i am offended')

            elif 'yes' in msg.content.lower():
                await msg.reply(f'thanks {msg.mention} but we should just be friends')
            tagged_is_lover.discard(msg.author)
