from jsonhandler import FileIO
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
            initial_channels=[],
           # port=8080,
           # webhook_server=True,
           # local_host='http://localhost',
           # external_host=f"http://{PUBLIC_IP}",
           # callback="89899189f08cc4e56b8d610c96fd3da08"




        )
        self.custom_cmd_file = FileIO("./customcommands.json")
        self.customcommands = self.custom_cmd_file.data

    async def event_ready(self):
        print(f"Bot is online!")
        ws = bot._ws  # this is only needed to send messages within event_ready
        await bot.join_channels(channels=['lisarei'])
      #  await ws.send_privmsg("lisarei", f"i am alive")
        print(f'Ready | {bot.nick}')
        # follow troubles
      #  await self.modify_webhook_subscription(mode=WebhookMode.subscribe, topic=UserFollows(to_id=178940115),lease_seconds=60)


    async def event_message(self, message):
        customcmd = message.content.split()
        if customcmd[0][1:].lower() in self.customcommands.keys():
            content = self.custom_cmd_file[customcmd[0][1:].lower()]
            formatted = content.format(ctx=message)
            await message.channel.send(formatted)
            return

        await self.handle_commands(message)


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
