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
            await ctx.channel.send("/me : welcome welcome thnx for stopping by <3")

    @commands.command(name="f")
    async def _f(self, ctx):
        if ctx.author.is_mod:
            await ctx.channel.send(
                "/me : thank u for following - is what the bot will say all by itself when we figure out webhooks...")

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
            f'time is  a social construct but here u go, it is: {(datetime.datetime.now()).strftime("%H:%M, %A %d/%m")}... gmt+1 babyy')

    @commands.command(name="list")
    async def _list(self, ctx):
        await ctx.channel.send(f"/me : your wish is my command, use: {', '.join(self.bot.commands)}")

    # @commands.command(name="timer")
    #async def _timer(self, ctx):
     #   await ctx.channel.send(f"/me : starting your timer: {timerrr}")


@commands.cog(name="Memory")
class Memory:
    # This class abuses the fact we not bot has a .memory item
    # I would not normally recommend coding this way

    def __init__(self, bot: TwitchBot):
        print(f"Module Memory loaded")
        self.bot = bot

    # Mod Only commands
    @commands.command(name="update")
    async def _update(self, ctx, key, *args):
        if not ctx.author.is_mod:
            return

        value = " ".join(args)
        self.bot.memory.set(key, value)
        print(f"Updated {key} to '{value}'")
