from twitchbot import Command


# links
@Command('github', aliases=['gb', 'git', 'gh', 'g', 'code'])
async def cmd_function(msg, *args):
    await msg.reply('come bully me at https://github.com/TheLisaRei/robotrei lisare1Heart ')


@Command('invite')
async def cmd_function(msg, *args):
    await msg.reply(
        'in game channel = LisaRei, ign = xymfa, and join w my link https://www.eveonline.com/signup?invc=046f680f-889d-4949-9a19-a383f98045e2 for one MILLION free skill points lisare1Heart ')


@Command('discord', aliases=['d'])
async def cmd_function(msg, *args):
    await msg.reply(
        'come hang out on discord! https://discord.com/invite/YuXqUR6 or use !dw to whisper the link to urself lisare1Heart ')


@Command('twitter', aliases=['t', 'bird'])
async def cmd_function(msg, *args):
    await msg.reply('follow me on twitter https://twitter.com/thelisarei lisare1Heart ')


@Command('instagram', aliases=['i', 'insta', 'ig'])
async def cmd_function(msg, *args):
    await msg.reply('my insta is: https://www.instagram.com/thelisarei/ lisare1Heart ')

@Command('youtube', aliases=['yt'])
async def cmd_function(msg, *args):
    await msg.reply('pls follow my youtube channel, i need 100 subscribers to make a non ugly url for it aaaaa: https://www.youtube.com/channel/UCyLCa__OaneD4kTOjJA-8og ')

@Command('donate', aliases=['paypal', 'tip', 'money'])
async def cmd_function(msg, *args):
    await msg.reply('please sir may i have some money *shakes cup* https://streamlabs.com/lisarei/tip or bitcoin in description  lisare1Heart ')
