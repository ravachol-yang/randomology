# text_handler.py
from telebot import TeleBot
from telebot.types import Message

from app.models.text import Text

# invoke with "/text" command
def get_random_text(message: Message, bot: TeleBot, data:dict):
    # pretend to be typing
    bot.send_chat_action(message.chat.id, "typing")
    # get options from message
    options = data['options']
        
    text = Text(bot, message)
    text.generate(options).send()

# invoke with "/mono"
def get_random_text_mono(message: Message, bot: TeleBot, data:dict):
    # pretend to be typing
    bot.send_chat_action(message.chat.id, "typing")

    options = data['options']
    
    mono = Text(bot, message)
    mono.generate(options)
    mono.to_mono().send(parse_mode="MarkdownV2")
