
from bot import TwitchBot
from twitchio.ext import commands
import datetime

@commands.cog(name="Moderation")
class Moderation:

    def __init__(self, bot: TwitchBot):
        print(f"Module Moderation loaded")
        self.bot = bot

    @commands.command(name="test")
    async def _test(self, ctx):
        if ctx.author.is_mod:
            await ctx.channel.send("pong!")

    @commands.command(name="love")
    async def _love(self, ctx):
        await ctx.channel.send("i love u!")

    @commands.command(name="hate")
    async def _hate(self, ctx):
        await ctx.channel.send("i hate u!")

    @commands.command(name="time")
    async def _time(self, ctx):
        await ctx.channel.send(f' time is  a social construct but here u go {(datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")}')


def setup(bot):
    bot.add_cog(Moderation(bot))
