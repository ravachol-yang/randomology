# info_handler.py

from telebot import TeleBot
from telebot.types import Message

from app.models.text import Text
from configs import templates

def get_info(message: Message, bot: TeleBot):
    bot.send_chat_action(message.chat.id, "typing")

    name = message.from_user.first_name
    id = message.from_user.id

    text = Text(bot, message)
    text.set_content(templates.INFO_MESSAGE.format(name=name, id=id))
    
    text.send(parse_mode="MarkdownV2")
