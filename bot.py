from twitchbot import BaseBot, load_commands_from_directory
from twitchbot import event_handler, Command, Event, Message, Channel


@event_handler(Event.on_user_join)
async def on_user_join(user: str, channel: Channel):
    print(f'{user} joined')



if __name__ == '__main__':
    load_commands_from_directory('./commands')
    BaseBot().run()