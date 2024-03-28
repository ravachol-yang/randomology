"""
base.py
the Base model
""" 

from telebot import TeleBot
from telebot.types import Message

class Base:

    def __init__(self,
                 bot:TeleBot = None,
                 message:Message = None):
        self.__bot = bot
        self.__message = message

    
    # get content of this object
    def content(self):
        return self._content

    # generate content
    def generate(self):
        raise NotImplementedError

    # send the message
    def send(self, **kwargs):
        send_me = getattr(self.__bot, "send_"+self.MSG_TYPE)
        send_me(self.__message.chat.id, self._content, **kwargs)
