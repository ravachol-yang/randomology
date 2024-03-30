from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware
from telebot.types import InlineQuery
from telebot.types import Message

class OptionMiddleware(BaseMiddleware):
    def __init__(self):
        self.update_types = ['message', 'inline_query']

    def pre_process(self, message, data):

        # if it's an inline query
        if isinstance(message, InlineQuery):
            msg_text = message.query
            if msg_text == "":
                msg_text = "placeholder"
            if msg_text[0] == '/':
                options = msg_text.split(" ",1)
                options.pop(0)
            else:
                options = [msg_text]
            
        # if it's a message
        elif isinstance(message, Message):
            msg_text = message.text
            options = msg_text.split(" ",1)
            options.pop(0)

        opt_data = dict({"bool_options": False,
                        "options":[]})
        if options:
            # takes the option string
            opt_str = options[0]
            try:
                # if user input options are in binary
                opt = bin(int(opt_str, 2))[2:]
            except ValueError:
                try:
                    # if user input options are in hex
                    opt = bin(int(opt_str,16))[2:]
                except ValueError:
                    # if it's in plain string
                    opt = opt_str
            # build binary array and not too long
            if opt.isdigit():
                # the last 16 options
                opt = opt[-16:]
                # set the flag to true
                opt_data["bool_options"] = True
                for i in opt.zfill(16):
                    opt_data["options"].append(bool(int(i)))
            else:
                opt_data["options"].append(opt)

        data["options"] = opt_data

    def post_process(self, message, data, exception=None):
        pass
