 # member_hander.py

from telebot import TeleBot
from telebot.types import Message

from app.models.text import Text
from configs import templates

# invoke when new member joins
def get_welcome(message:Message, bot:TeleBot):
    # typing ...
    print("welcome")
    bot.send_chat_action(message.chat.id, "typing")
    new_member = message.new_chat_members
    welcome = templates.WELCOME_MESSAGE.format(name=new_member[0].first_name,
                                               id=new_member[0].id)
    text = Text(bot, message)
    text.set_content(welcome)
    text.send(parse_mode="MarkdownV2")
    
