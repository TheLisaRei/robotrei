from twitchbot import Command, Message


@Command('bye', aliases=['goodbye', 'seeya'])
async def cmd_function(msg: Message, *args):
    mention = ''
    goodnight = False

    if len(args) > 0 and args[0].startswith('@'):
        mention = args[0]
    
    if len(args) > 1 and args[1].lower() == 'goodnight':
        goodnight = True

    message = f'Bye {mention}! Thank you for visiting my channel. See you next time.'

    if goodnight:
        message += ' Good night!'
    
    await msg.reply(message)