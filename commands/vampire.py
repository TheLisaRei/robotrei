from twitchbot import Command, Message, choice
import random


# vampire stuff



@Command('vampire', aliases=['whichvampire'])
async def cmd_function(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    print(target)
    await msg.reply(f'{target} ' + choice(['Jasper from Twilight who was a confederate soldier. but hot so yanno.. redeemable. very moody',
               'Rosalie from Twilight.. hottest bad bitch of em all. congrats',
               'lol Bella Swan. u dumbass. but like shes okay later',
               'Nosferatu... the only vampire i DONT want to sleep with',
               'Damon Salvatore and im in love with you. deeply... lets kiss? haha jk... unless?,,, ;)',
               'Stefan Salvatore, very cool.. can i pls have Damons number???',
               'Dracula.. classic. vampire daddy. nothing else to say. vanilla ice cream of vampires',
               'Eric Northman... is this true love?? sir pls bite me... i am yours',
               'Bill from true blood. not hot. no clue how sookie was into him, he srs looks dead. ugh. team Eric',
               'Pamela from true blood. banging latex lady. be my sugarmommy pls',
               'Tanya from Twilight, u fucking RAT... snitches get stitches... u deserved ur fate',
               'not even a vampire, u are a filthy werewolf. gross. moonboy.',
               'Godric from True Blood, you have seen it all, unmoved mover. peaceful being'
               ]))
