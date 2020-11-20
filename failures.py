@commands.command(name="followage")
async def _followage(self, ctx):
    # follow = await self.bot.get_follow(ctx.author.id, 178940115)
    follow = await self.bot.get_followers(178940115)

    print(follow)


@commands.command(name="follow")
async def _follow(self, ctx):
    await ctx.channel.send("something")


# https://api.twitch.tv/helix/users/follows?to_id=178940115