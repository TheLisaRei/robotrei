from twitchbot import Command, Message, custom_predicate, choice



@Command('karma', aliases=['reincarnation', 'next', 'nextlife'])
async def cmd_function(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    await msg.reply(f'{target} you will be reincarnated as ' + choice([
        'a worm for your thought crimes.... be happy u even got a worm...',
        'a majestic eagle living by the grand canyon, you are a good person',
        'a naked mole rat because you did not help that lady get a stroller onto the bus in 2009',
        'a snake - all of those times you betrayed your friends coming back to you, huh?',
        'a golden retriever that lives with a middle class american family.. life is good',
        'a mean little girls hamster... she squeezes u too hard but not hard enough to kill you so you live in misery',
        'a chicken, hope youre not scared just at the thought of it, you chicken',
        'your exes second child... you will be forced to witness her happiness with her husband.. a true hell. but also she will love you for once since you will be her child. once last time inside of her',
        'one of those eye floaters - technically not even an animal, but do you really deserve one?',
        'a whale. at least your weight didnt change i guess',
        'a wolf because you said u would rather be a werewolf than a vampire so now you are a smelly dog',
        'a wolf, because you always want to awoo... TOO BAD THIS IS AN AWOO-FREE ZONE, YOURE GETTING A $500 FINE',
        'a new york city pigeon. absolutely disgusting. filthy creature in the next life just like you are one in this life',
        'a volcano shark... thats pretty hot',
        'the chihuahua of the girl who used to bully you in HS, so now u get to lick the inside of her mouth because she is one of those gross people who kiss dogs',
        'your dad... dont ask me how this works',
        'a beautiful butterfly, head empty no thoughts only flowers. love it',
        'a panda, but you are kept at a zoo and since pandas are endangered, the zoo keepers keep trying to mate you with other pandas while they watch. its kinda awkward. thats what you get for walking in on your friend in the upstairs bedroom of that 2014 house party',
        'a panther! it seems like your cougar fetish transferred to your next life ;)',
        'a bear!!! no not the animal. the gay man type. you will have much more fun in the next life!!! hot!!!',
        'a cat, but your owner keeps over feeding you and since you are a dumb feline u cannot stop eating so you are a chonky boiii :(',
        'a butterfly. some would think youre pretty but youre just really dumb',
        'a ferret called Bunny, you keep eating smaller animals because your owner believes that ferrets are like dogs and can just hang out unsupervised. but you are a menace and have a taste for blood. not sure what that says about your current way of life....',
        'a bedbug. at least getting some action in your next life!',
        'a horse owned by an insane horse lady, you have never been loved like this as a human',
        'a mosquito, you will bite and infect with malaria the little girl who would have grown up to cure cancer, she dies of malaria induced fever at 8 years old. you have caused millions of deaths and unimaginable suffering but it is nothing compared to the pure evil you will manage to cause in this life',
        'a tapeworm. your parasitic lifestyle does not change. i feel sorry for your parents',
        'a male duck, you will spend the rest of your wet and cold. also rapey... so rapey...',
        'a giant moose, you get to walk around the pristine nature of northern canada and be majestic... you deserve it! congrats',
        'a parrot, your owner is a lonely old man and he loves you so much and you have a beautiful existence bringing joy to this sweet widower',
        'a unicorn! unfortunately youre the last one, so your life will be long and lonely - just like your current life',
        'a lion, you will have a nice majestic life until your lion brother trows you off of a cliff for saying lion king is a boring movie',
        'a hobbit because you forced your girlfriend to watch Lord of the Rings... the whole 12 hours of it.... u animal.... u are a life sized hobbit in the minecraft world and your textures dont match at all',
        'Edward Cullen from Twilight bc you laughed at Lisas vampire fetish. enjoy the sparkles lolll',
        'a bat. some weirdo will disturb your home to fulfill his latex fetish',
        'a hippie hipster who doesnt believe in deodorant. nothing will change his mind. but u know... yet u cannot change... also u play the ukulele to pick up women at the local vegan store and it never works',
        'a cute little spider. too bad you live in a house with a family of arachnophobes'



    ]))
