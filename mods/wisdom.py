from twitchbot import Command, Message, custom_predicate, choice


@Command('wisdom')
async def cmd_wisdom(msg: Message, *args):
    await msg.reply(
        f'Oh no {msg.mention}, you were walking down the street you saw a black cat run across the road, do you turn back or keep walking? [type turn/walk]')
    response = await msg.wait_for_reply(
        custom_predicate(
            lambda m: any(text in m.parts for text in ('turn', 'walk')), msg=msg
        ), timeout=30
    )

    if not response.is_message:
        await msg.reply(
            f'oh no {msg.mention}, stopped in the middle of the street... Bryson was driving home in his daddys SUV and well.... dont worry he will get 20 hours of community service for ur death ')
        return

    if 'turn' in response.raw_value.parts:
        await msg.reply(choice([
            f'wise choice, {msg.mention}, young one.... you turn without looking and you get hit by a bus u did not see coming. such is fate',
            f'ohh you are turning back, wise choice {msg.mention}, you were able to escape your fate... for now...',
            f'only cowards try to escape their destiny, {msg.mention}... you become a citizen of france as your punishment. now you are home. go eat a baguette frogman',
            f'hmmmm so you are choosing to follow the devils path, it leads you to a woman in the park, she offers you something... you are led astray {msg.mention} ... you wake up 4 months later with a meth addiction',
            f'turn back? I hear you {msg.mention}, Id do the same... we should hold hands as we turn back... haha just joking... unless??? ;))',
            f' okay {msg.mention}, you turn back and walk back home... your spouse is mad bc you were supposed to buy lemons... but hey you saw a black cat so what else could u have done',
            f'turn back!!!! {msg.mention} you akwardly do an 180 and walk the other way. weirdo. but hey whatever keeps u safe. who cares what people think',
            f'ohh of course you turned back {msg.mention}, i knew you would.. my mother was right about you, you just give up on things and take the easy way out... thats why it never could have worked between us... you know my therapist says you have avoidant attachment type..,',
            f' lol {msg.mention} you turn back and see Chad, Bradson and Bryson from your High School walking towards you and as they are getting closer, you trip and fall into a puddle face first and they all laugh and point your way, how emmbarrrasssssinggg.'
        ]))

    elif 'walk' in response.raw_value.parts:
        await msg.reply(choice([
            f'mmm a brave soul... too brave. a grand piano falls on you from the heavens above and you are smashed into the pavement, rest in peace meat goo {msg.mention}',
            f'oh dear oh dear did you not see the cat? you trip over the poor feline and fall into wet concrete, {msg.mention}, what a day...',
            f'these boots are made for walking and walking is what they will do... {msg.mention} you become a street walker for the night. your price is set at $20, enjoy',
            f'ooo nice choice {msg.mention}, black cats actually bring luck. u find a 5 dollar bill and buy a strawberry jam donut',
            f'you walk by and nothing happens, {msg.mention} how boring...',
            f'ohh you walk closer and the kitty meows at u {msg.mention}, it must be homeless!!! you adopt the kitty and name it Lucky. congrats',
            f'ok ok ok {msg.mention} u walk and meet a lady frantically searching for her lost ferret called Bunny who escaped and ate her neighbors hamster and she needs to find Bunny before the neighbors do. what a bizarre situation. why would u voluntarily own a ferret. their tiny hands r creepy. but u dont ask these questions bc she seems mildly deranged. is the ferret even real? what if shes having a mental heath episode and u r accidentally enabling her? hmmmm.... you are torn away from your pondering by a SHARP PAIN in your foot as a ferret bites your toe. seems like it was real after all... the lady picks up Bunny and kisses the beast on its little bloody mouth. you are traumatizzed and might have rabies now....',
            f'so {msg.mention} you decide to walk back and you see your first love pushing a pram with her husband, she looks so happy, you didnt even know she was married now... they look so happy... it could have been you... if only you had done things differently.. you go home to your empty apartment and sit on the only chair you own by a wonky table and reflect on how lonely and sad you are',
            f'you walk and walk and walk {msg.mention} and you find yourself in a graveyard so you take a stroll..... OMGGGGGG what is that!!!! oh no.... it couldnt be..... a gravestone with your name on it and todays date????? what is happening????'
        ]))
