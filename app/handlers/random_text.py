# random_text.py
from telebot import TeleBot
from telebot.types import Message

# for generating random strings
import string
import random

#  random text generater for the following handlers
def generate_random_text():
    length = random.randint(30,120)
    return ''.join(random.choices(string.ascii_letters +
                                  string.digits +
                                  string.punctuation, k=length))

# invoke with "/random_text" or "/random" command
def get_random_text(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, generate_random_text())
