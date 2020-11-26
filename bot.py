from twitchbot import BaseBot, load_commands_from_directory
from twitchbot import event_handler, Command, Event, Message, Channel, Mod, PollData

# works
@event_handler(Event.on_user_join)
async def on_user_join(user: str, channel: Channel):
    print(f'{user} joined')
    # await channel.send_message(f'hi @{user}')

# dont know if it works but it should?
@event_handler(Event.on_channel_subscription)
async def on_channel_subscription(subscriber: str, channel: Channel, msg: Message):
    await channel.send_message(f'omg @{subscriber} just subscribed wooowww thank uuu')

# only for the bot poll but works
@event_handler(Event.on_poll_started)
async def on_poll_started(channel: Channel, poll: PollData):
    print('pollllioo')




if __name__ == '__main__':
    load_commands_from_directory('./commands')
    BaseBot().run()
