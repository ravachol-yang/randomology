# info_handler.py

from telebot import TeleBot
from telebot.types import Message

from app.services.info_service import generate_info

def get_info(message: Message, bot: TeleBot):
    name = message.from_user.first_name
    id = message.from_user.id
    info = generate_info(name, id)
    bot.send_message(message.chat.id, info, parse_mode="MarkdownV2")
