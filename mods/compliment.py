from twitchbot import Command, Message, custom_predicate, choice


@Command('compliment', aliases=['compliments', 'nice'])
async def cmd_function(msg: Message, *args):
    target = msg.arg_or_default(0, msg.author)
    print(target)
    await msg.reply(f' lisare1Heart {target} lisare1Heart  ' + choice([
        'you have really nice feet ',
        'you are your moms favorite',
        'you fingers are the correct length in proportion to your hands',
        'you r good enough, u are smart enough, and god damn it, people like you',
        'you have nice teeth',
        'people enjoy your personality',
        'if u were murdered, your friends and family would say you lit up the room and would give anyone the shirt off of your back on the CrimeWatchTV episode about your case and they would not be lying',
        'your morning breath is as fresh as mint',
        'your exes mom still asks your ex about you, you were her favorite',
        'you can make almost any pants look good, pixar mom style',
        'you look good today baby i wish i was there with you are u into robots bc i think we could make us work if u just gave me a chance oh wait i got carried away disregard... unless....?',
        'you have intelligent eyes',
        'you have great ideas',
        ' Youre a true gift to the people in your life.',
        ' The way you carry yourself is truly admirable.',
        'Simply knowing you has made me a better person.',
        ' Your heart must be 10 times the average size',
        ' I tell other friends how wonderful you are.'
        ' You deserve everything you’ve achieved.',
        'On a scale from 1 to 10, you’re an 11.',
        'you are a good driver',
        'you smell good',
        'i would trust you with a puppy',
        'i bet babies smile at you',
        'You code like a hacker on a coffee overdose.',
        'Your smile is proof that the best things in life are free.',
        ' I trust you more than https',
        'i bet you write documentation for your projects',
        'i wish we were siblings',
        'If there is one thing I like about you, its that I like more than one thing about you.',
        'you probably recycle',
        'you have nice ears',
        'I looked in my error log but I couldnt find you.',
        'you make many people happy',
        'Bob Ross would have been friends with you!',
        'i value the time i get to spend with you',
        'your ears are the correct size to compliment your head shape',
        'you could pull any haircut off',
        'your natural haicolor is what many people wish they were born with',
        'i bet all your houseplants are thriving!!',
        'u are a good child to your parents and they are so proud of u',
        'your children will NOT need therapy after your parenting, congratulations',
        'You’re Even More Beautiful On The Inside Than You Are On The Outside.',
        ' When You’re Not Afraid To Be Yourself Is When You’re Most Incredible.',
        '. If You Were A Box Of Crayons, You’d Be The Giant Name-Brand One With The Built-In Sharpener.',
        'You’re A Candle In The Darkness.',
        'Actions Speak Louder Than Words, And Yours Tell An Incredible Story.',
        'In High School, I Bet You Were Voted “Most Likely To Keep Being Awesome.”',
        'You’re Really Something Special.',
        'Babies And Small Animals Probably Love You.',
        ' If Cartoon Bluebirds Were Real, A Couple Of ’Em Would Be Sitting On Your Shoulders Singing Right Now.',
        'You’re More Fun Than A Ball Pit Filled With Candy.'

    ]))
