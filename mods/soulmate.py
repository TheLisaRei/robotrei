from twitchbot import Command, Message, custom_predicate, choice



# fix user input later

@Command('soulmate')
async def cmd_soulmate(msg: Message, *args):
    await msg.reply(
        f'welcome to my fortune telling tent, i am madame Rei, i am here to tell you about your soulmate, but first tell me {msg.mention}, what is your preference? [type girl/boy]')

    response = await msg.wait_for_reply(
        custom_predicate(
            lambda m: any(text in [p.lower() for p in m.parts] for text in ('girl', 'boy')), msg=msg
        ), timeout=30
    )


    if not response.is_message:
        await msg.reply(f'u have not responded {msg.mention}, seems like u are not ready for this knowledge ')
        return

    if 'girl' in response.raw_value.parts:
        await msg.reply(choice([
            f'mmm {msg.mention}, the crystal ball tells me your soulmate is mmmmmm ohh yess i see BROWN EYES... beautiful brown eyes...',
            f'ohh {msg.mention} you are so lucky she is incredibly SMART, a true intellectual... you might meet at a conference on AI actually',
            f'so {msg.mention} u want to know something about ur soulmate hmm? well my crystal ball is on strike today but my intuition tells me you will meet her before the year ends',
            f'i see i see that you will find true love!! {msg.mention} but you will lose her bc u forget to cherish her every day!! but now that i have told u the secret.. you must change your fate!!',
            f'hmm {msg.mention} the devil whispered in my ear that your true love is Rosalie from Twilight... how embarassing.. do you have a vampire fetish or something??? shes not even real',
            f'see the angels dont want me to tell you who your soulmate is.. {msg.mention} but i can tell you who your divorce attorney will be!! its Greenhill & partners in Rochester, NY... do w that what u will. she will be awarded full custody of ur parrot... beware',
            f' oh no {msg.mention}, your soulmate was that girl u saw on the subway in 2014... you will never meet her again',
            f' your soulmate is the last lady you bought a burger from, {msg.mention}, I dont care if u dont like her and she could be ur mom, it is fate stop fighting it',
            f' sorry {msg.mention}, she has a boyfriend right now but she will see the light soon... he just started playing WoW again and stopped brushing his teeth... your time is coming',
            f' oh no {msg.mention}... your soulmate plays LoL, i am so sorry, i will give you a full refund for my services, that is really unfortunate. our society places too much value on being in a romantic relationship, theres nothing wrong with staying single forever. its really the better option for you all thing considered',
            f'wow {msg.mention} your soulmate is your least favorite ex. you fucked up, call and apologize for everything'
        ]))

    elif 'boy' in response.raw_value.parts:
        await msg.reply(choice([
            f' hmm i seee.. i seee.. your soulmate has a bedframe (and mattress w no stains) and several plants... {msg.mention} very rare',
            f' ohhh a man?? okay okay let me recalibrate my crystal ball.. now i see.. he is taller than you.. {msg.mention}  he likes sports and travel.. has a golden retriever? damn i really need to work on my male soulmate visions...',
            f'ohh {msg.mention} your soulmates name is Nigel, do with that what you will',
            f' you have come to the right place!! {msg.mention} i was just thinking about you!! i had a dream about your love life! so much information.... i just need a small payment before i tell you... wait where are you going???',
            f' so.. idk how to tell u {msg.mention}, you will meet a man in january, everything will be fine for a little while, not amazing but fine.. until u talk about politics and find out hes kinda a nazi and lowkey hates women... then youll be single for a while... by august u figure out u actually like women and meet a girl on tinder... you will move in together after a week. she was ur soulmate all along',
            f' omg {msg.mention} i know who ur soulmate is!! his name is Jacob Black and he was born in London October 12 1828!! oh wait... 1827... oh no... welp. ur soulmate is long dead. u will never find anyone else... no no dont cry... get an ouija board or something?',
            f'hmm {msg.mention} the devil whispered in my ear that your true love is Jasper from Twilight... how embarassing.. do you havew a vampire fetish or something??? hes not even real and he was a CONFEDERATE soldier.. eww',
            f' oh no {msg.mention}... your soulmate plays LoL, i am so sorry, i will give you a full refund for my services, that is really unfortunate. our society places too much value on being in a romantic relationship, theres nothing wrong with staying single forever. its really the better option for you all thing considered',
            f' hmmmm idk how to tell you this but your soulmate is a furry {msg.mention}, the worst thing is that his fursona is a bird. i am a very tolerant being but it is disturbing... the bird part esp'
        ]))
