from jsonhandler import FileIO

from bot import TwitchBot
from twitchio.ext import commands
import datetime


@commands.cog(name="Moderation")
class Moderation:

    def __init__(self, bot: TwitchBot):
        print(f"Module Moderation loaded")
        self.file = FileIO("./customcommands.json")
        self.customcommands = self.file.data
        self.bot = bot

    @commands.command(name="test")
    async def _test(self, ctx):
        if ctx.author.is_mod:
            await ctx.channel.send("pong!")

    @commands.command(name="w")
    async def _w(self, ctx):
        if ctx.author.is_mod:
            await ctx.channel.send("welcome welcome thnx for stopping by <3")

    @commands.command(name="f")
    async def _f(self, ctx):
        if ctx.author.is_mod:
            await ctx.channel.send(
                "thank u for following - is what the bot will say all by itself when we figure out webhooks...")

    @commands.command(name="customcmd")
    async def _customcmd(self, ctx, cmd, *, content):
        if ctx.author.is_mod:
            if cmd[0][1:].lower() in self.customcommands.keys():
                await ctx.send(f"Successfully created customcommand {cmd}")
                self.file.save()
            else:
                await ctx.send(f"The command {cmd} already exist")


    @commands.command(name="time")
    async def _time(self, ctx):
        await ctx.channel.send(
            f' time is  a social construct but here u go {(datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")}')

    @commands.command(name="list")
    async def _list(self, ctx):
        await ctx.channel.send(f"your wish is my command, use: {', '.join(self.bot.commands)}")


def setup(bot):
    bot.add_cog(Moderation(bot))

