from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware
from telebot.types import InlineQuery
from telebot.types import Message

class OptionMiddleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message', 'inline_query', 'chat_new_members']

    def pre_process(self, message, data):

        # if it's an inline query
        if isinstance(message, InlineQuery):
            msg_text = message.query
            options = [msg_text]
            
        # if it's a message
        elif isinstance(message, Message):
            msg_text = message.text
            options = msg_text.split(" ",1)
            options.pop(0)

        if options:
            # remove spaces and make options list
            options = options[0].replace(" ","")
            options = options.split(",")

        data['options'] = options

    def post_process(self, message, data, exception=None):
        pass
