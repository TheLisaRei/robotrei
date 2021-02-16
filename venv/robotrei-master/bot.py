# DO NOT TOUCH THIS
from twitchbot import BaseBot, event_handler, Command, Event, Message, Channel,  PubSubTopics, Mod, get_pubsub


# all this might conflict with the pubsub subscribe thing

# user joins - prints in run
@event_handler(Event.on_user_join)
async def on_user_join(user: str, channel: Channel):
    print(f'{user} joined')


# maybe remove this bc it hurts my feelings
@event_handler(Event.on_user_part)
async def on_user_part(user: str, channel: Channel):
    print(f'{user} left')



# DO NOT TOUCH THIS EVER
if __name__ == '__main__':
    BaseBot().run()
