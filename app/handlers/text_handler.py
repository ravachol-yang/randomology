# text_handler.py
from telebot import TeleBot
from telebot.types import Message

from app.models.text import Text

from app.handlers.utils import get_options

# invoke with "/text" command
def get_random_text(message: Message, bot: TeleBot):
    # pretend to be typing
    bot.send_chat_action(message.chat.id, "typing")
    # get options from message
    options = get_options(message.text, True)
        
    text = Text(bot, message)
    text.generate(options).send()

# invoke with "/mono"
def get_random_text_mono(message: Message, bot: TeleBot):
    # pretend to be typing
    bot.send_chat_action(message.chat.id, "typing")

    options = get_options(message.text, True)
    
    mono = Text(bot, message)
    mono.generate(options)
    mono.to_mono().send(parse_mode="MarkdownV2")
