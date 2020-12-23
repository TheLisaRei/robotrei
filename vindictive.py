from asyncio import Task
from twitchbot import Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from twitchbot import session

__all__ = ('Vindictive')
# function stuff goes here? ['']


class Vindictive(Base):
    __tablename__ = 'vindictive'

    id = Column(Integer, nullable=False, primary_key=True)
    channel = Column(String(255), nullable=False)
    user = Column(String(255), nullable=False)
    goodbot = Column(Integer, nullable=False)
    badbot = Column(Integer, nullable=False)

    @classmethod
    def create(cls, channel: str, user: str):
        return Vindictive(channel=channel.lower(), user=user)







