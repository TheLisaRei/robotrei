from twitchbot import Command, Message

# lovely goodnight and bye command
@Command('bye', aliases=['goodbye', 'seeya'])
async def cmd_function(msg: Message, *args):
    mention = ''
    goodnight = False

    if len(args) > 0 and args[0].startswith('@'):
        mention = args[0]
    
    if len(args) > 1 and args[1].lower() == 'goodnight':
        goodnight = True

    message = f'byeeee {mention}! Thank you for hanging out. see you tomorrow  '

    if goodnight:
        message += ' good night! and sweet dreams'
    
    await msg.reply(message)

# welcome
@Command('welcome', aliases=['wel', 'ww'])
async def cmd_function(msg: Message, *args):
    mention = ''
    back = False

    if len(args) > 0 and args[0].startswith('@'):
        mention = args[0]

    if len(args) > 1 and args[1].lower() == 'back':
        back = True

    message = f'welcome welcome {mention}! thank you for popping in. make yourself at home  '

    if back:
        message += ' im so happy to see u come back here '

    await msg.reply(message)