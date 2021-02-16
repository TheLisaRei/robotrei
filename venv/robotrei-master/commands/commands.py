from twitchbot import Command, Message
import asyncio
import datetime
import zoneinfo

# TIMEZONE LOADING
available_timezones = zoneinfo.available_timezones()


# start pomodoro timer
@Command('tomato')
async def cmd_function(msg, *args):
    await msg.reply(
        f'ok {msg.mention} you should work/study for the next 25min, ill notify u when its time for a break')
    await asyncio.sleep(1500)
    await msg.reply(
        f' {msg.mention} congrats, your work time has finished, enjoy a 5min break, ill tell you when its over')
    await asyncio.sleep(300)
    await msg.reply(f' {msg.mention} congrats, you completed a cycle, use !tomato to start again')


# hate
@Command('amazon', aliases=['bezos', 'jeff'])
async def cmd_function(msg, *args):
    await msg.reply('amazon is a terrible company')


@Command('elon', aliases=['musk', 'muskrat'])
async def cmd_function(msg, *args):
    await msg.reply('elon musk should be made into a leather couch and left by the trashcan')


# game wiki

@Command('eve', aliases=['e', 'eveonline'])
async def cmd_function(msg, *args):
    await msg.reply(
        'Eve Online is a space-based, persistent world massively multiplayer online role-playing game developed and published by CCP Games. Players of Eve Online can participate in a number of in-game professions and activities, including mining, piracy, manufacturing, trading, exploration, and combat.')


@Command('isk')
async def cmd_function(msg, *args):
    await msg.reply('send ISK to "xymfa" and i will not double it')


@Command('games', aliases=['game'])
async def cmd_function(msg, *args):
    await msg.reply('stardew valley, eve online and some minecraft... if u wanna play w me go to my discord')


@Command('stardew')
async def cmd_function(msg, *args):
    await msg.reply(
        'Stardew Valley is an open-ended country-life RPG! Youve inherited your grandfathers old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.')


# basic react stuff

@Command('me')
async def cmd_function(msg, *args):
    await msg.reply(f'you exist {msg.mention}')


@Command('coffee')
async def cmd_function(msg, *args):
    await msg.reply(f'lol u wish {msg.mention}... i am not ur secretary...  go make ur own coffee u lazy kiddo')


@Command('tea')
async def cmd_function(msg, *args):
    await msg.reply('vanilla rooibos tea!')


@Command('upset', aliases=['angry'])
async def cmd_function(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    print(target)
    await msg.reply(f'{target} is upset :( what did u all do? angry!? unacceptable... terrible!!')


@Command('panic')
async def cmd_function(msg, *args):
    await msg.reply('AAAAAAAAAAAAAAAAAAAAAAA')


@Command('indent', aliases=['indentation'])
async def cmd_function(msg, *args):
    await msg.reply('pssst @lisarei doesnt know how to indent pass it on')


@Command('hug')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u have been hugged @{msg.mentions[0]}  ')


@Command('cake')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u have been given some yummy cake @{msg.mentions[0]} pls enjoy!!')


@Command('poke')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u have been poked @{msg.mentions[0]}  ')


@Command('kiss')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(
        f'ugh u have been kissed @{msg.mentions[0]}... ew. unsanitary.. its covid season this is not allowed.')


@Command('kill')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'lol u have been killed @{msg.mentions[0]}... rip i guess heh')


@Command('resurrect')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'ooo u have been brought back from the dead @{msg.mentions[0]}... freaky lol')


@Command('bully')
async def cmd_function(msg, *args):
    print(msg.mentions)
    await msg.reply(f'u suck and cant sit with us @{msg.mentions[0]}... >:( ')


@Command('sorry')
async def cmd_function(msg, *args):
    await msg.reply(f'hmmm i dont know if i forgive you... robots never forgive or forget')


@Command('die')
async def cmd_function(msg, *args):
    await msg.reply('oh wow... u big meanie.... speechlesssss')


@Command('say')
async def cmd_say(msg, *args):
    allowed_users = {'lisarei'}
    if msg.author in allowed_users:
        await msg.reply(' '.join(args))


# not all cities work, no india or china for some reason

@Command('time', aliases=['timezone'])
async def cmd_function(msg, *args):
    if not args:
        await msg.reply(
            f'time is  a social construct but here u go, it is: {(datetime.datetime.now()).strftime("%H:%M, %A %d/%m")}... gmt+1 babyy')
        return

    place = " ".join(args)
    search_term = place.replace(" ", "_").lower()
    place_title = place.title()

    # Just doing a linear search through every single timezone in
    # the database, substring search on each.
    # yeah, there is room for improvement on this, to catch spelling
    # errors, for example.

    # NOTE: you may need to grab data from somewhere to get this
    # to work (I didn't look that deeply into it):
    # https://docs.python.org/3/library/zoneinfo.html#data-sources

    # also, maybe there is a database (or api) somewhere to be able
    # to look up _any_ city or town, and find the respective timezone.
    # as of right now, timezones are just searched through the standard
    # timezone names, and so the number of cities it can locate is
    # very small. Basically these (assuming the timezone database we
    # have here, in python, on the machine running this code, is the
    # same as this one - which I think it is..but I really don't know,
    # sorry):
    # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    found_timezone = None
    for zone in available_timezones:
        if search_term in zone.lower():
            found_timezone = zoneinfo.ZoneInfo(zone)
            break

    if found_timezone is None:
        await msg.reply(f" oh no I couldn't find timezone for \"{place_title}\"")
    else:
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        now_local = now_utc.astimezone(found_timezone)
        formatted_date = now_local.strftime("%H:%M, %A %d/%m")
        await msg.reply(f"current local time in {place_title}: {formatted_date}")
