from twitchio.ext import commands

from config import Config


# noinspection PyAbstractClass
class TwitchBot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=Config.TMI_TOKEN,
            client_id=Config.CLIENT_ID,
            nick=Config.BOT_NICK,
            prefix="!",
            initial_channels=[]
        )

    async def event_ready(self):
        print(f"Bot is online!")
        ws = bot._ws  # this is only needed to send messages within event_ready
        await bot.join_channels(channels=['lisarei'])
        await ws.send_privmsg("lisarei", f"i am alive")
        print(f'Ready | {bot.nick}')


# for each new file with commands add the file name into this list
modules = ['commands']

if __name__ == "__main__":
    bot = TwitchBot()
    for module in modules:
        try:
            bot.load_module(str(module))
        except Exception as e:
            print(e)
    bot.run()