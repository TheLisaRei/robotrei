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

    @commands.command(name="customcmd")
    async def _customcmd(self, ctx, cmd, *, content):
        if ctx.author.is_mod:
            if cmd[0][1:].lower() in self.customcommands.keys():
                await ctx.send(f"Successfully created customcommand {cmd}")
                self.file.save()
            else:
                await ctx.send(f"The command {cmd} already exist")

    @commands.command(name="love")
    async def _love(self, ctx):
        await ctx.channel.send("i love u!")

    @commands.command(name="hate")
    async def _hate(self, ctx):
        await ctx.channel.send("i hate u!")

    @commands.command(name="time")
    async def _time(self, ctx):
        await ctx.channel.send(
            f' time is  a social construct but here u go {(datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")}')


def setup(bot):
    bot.add_cog(Moderation(bot))
