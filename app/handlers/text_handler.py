# random_text.py
from telebot import TeleBot
from telebot.types import Message

from app.services.text_service import generate_random_text
import string

SPECIAL = ['_', '*', '[', ']', '(', ')', '~', '`', '<' , '>', '#', '+', '-', '=', '|', '{', '}', '.', '!' ]

# invoke with "/random" command
def get_random_text(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, generate_random_text())

# invoke with "/random_mono"
def get_random_text_mono(message: Message, bot: TeleBot):
    text = generate_random_text()
    # add an "\" before every special char for parsing markdown
    for i in SPECIAL:
        text = text.replace(i, "\\"+i)
    bot.send_message(message.chat.id, "`"+text+"`", parse_mode="MarkdownV2")
