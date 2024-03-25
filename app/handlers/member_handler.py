 # member_hander.py

from telebot import TeleBot
from telebot.types import Message

from app.services.member_service import generate_welcome

# invoke when new member joins
def get_welcome(message:Message, bot:TeleBot):
    # typing ...
    bot.send_chat_action(message.chat.id, "typing")
    new_member = message.new_chat_members
    welcome = generate_welcome(new_member[0].first_name, new_member[0].id)
    bot.send_message(message.chat.id, welcome, parse_mode="MarkdownV2")
