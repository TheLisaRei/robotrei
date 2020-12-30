# DO NOT TOUCH THIS
from twitchbot import BaseBot, event_handler, Command, Event, Message, Channel


# user joins - prints in run
@event_handler(Event.on_user_join)
async def on_user_join(user: str, channel: Channel):
    print(f'{user} joined')
    # await channel.send_message(f'hi @{user}')


# maybe remove this bc it hurts my feelings
@event_handler(Event.on_user_part)
async def on_user_part(user: str, channel: Channel):
    print(f'{user} left')


# subscriptions
@event_handler(Event.on_channel_subscription)
async def on_channel_subscription(subscriber: str, channel: Channel, msg: Message):
    await channel.send_message(f'omg @{subscriber} did something very cool. thank u.')


# will be updated - follows
@event_handler(Event.on_privmsg_received)
async def on_privmsg_received(msg: Message):
    allowed_users = {'streamlabs'}
    if 'Thank you for following' in msg.content and msg.author in allowed_users:
        await msg.reply('yes yes thank u for following! <3 i am the !bot of this channel')


# bits
@event_handler(Event.on_bits_donated)
async def on_bits_donated(self, msg: Message, bits: int):
    await msg.reply('thank you for cheering')


# DO NOT TOUCH THIS EVER
if __name__ == '__main__':
    BaseBot().run()
