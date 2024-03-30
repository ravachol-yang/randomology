"""
base.py
the Base model
""" 

from telebot import TeleBot
from telebot.types import Message

class Base:

    OPTIONS_AVAILABLE = []
    OPTIONS_DEFAULT = {}

    _options = dict(OPTIONS_DEFAULT)

    def __init__(self,
                 bot:TeleBot = None,
                 message:Message = None):
        self.__bot = bot
        self.__message = message

    
    # get content of this object
    def content(self):
        return self._content

    # set content
    def set_content(self, content:str):
        self._content = content

    # set options
    def set_options(self, options):
        if options["bool_options"]:
            opt = options["options"]
            # index for mapping from boolean array to options
            index  = 0
            for i in self._options:
                # change options accordingly, opt with be chopped to the last elements
                self._options[i]["enabled"] = opt[-len(self.OPTIONS_AVAILABLE):][index]
                index += 1
        else:
            # TODO: support non-bool options
            pass

        return self

    # generate content
    def generate(self):
        raise NotImplementedError

    # send the message
    def send(self, **kwargs):
        send_me = getattr(self.__bot, "send_"+self.MSG_TYPE)
        send_me(self.__message.chat.id, self._content, **kwargs)
