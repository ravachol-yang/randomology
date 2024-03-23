# info.py

from telebot import TeleBot
from telebot.types import Message

def get_info(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Hello, I'm a bot of Randomology ~")
