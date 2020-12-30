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
            f'turn back!!!!{msg.mention} you akwardly do an 180 and walk the other way. weirdo. but hey whatever keeps u safe. who cares what people think'
        ]))

    elif 'walk' in response.raw_value.parts:
        await msg.reply(choice([
            f'mmm a brave soul... too brave. a grand piano falls on you from the heavens above and you are smashed into the pavement, rest in peace meat goo {msg.mention}',
            f'oh dear oh dear did you not see the cat? you trip over the poor feline and fall into wet concrete, {msg.mention}, what a day...',
            f'these boots are made for walking and walking is what they will do... {msg.mention} you become a street walker for the night. your price is set at $20, enjoy',
            f'ooo nice choice {msg.mention}, black cats actually bring luck. u find a 5 dollar bill and buy a strawberry jam donut',
            f'you walk by and nothing happens, {msg.mention} how boring...',
            f'ohh you walk closer and the kitty meows at u {msg.mention}, it must be homeless!!! you adopt the kitty and name it Lucky. congrats',
            f'walk? hmm ok {msg.mention}, you walk down the road and... tune in after the AD break to find out what happens!!!'
        ]))
