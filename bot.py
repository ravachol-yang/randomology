# the randomology telegram bot

# config
from config import config

# handlers
from app.handlers.info import get_info
from app.handlers.random_text import get_random_text
from app.handlers.random_text import get_random_text_mono
from app.handlers.inline import inline_dispatch

# pyTelegramBotAPI
import telebot
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)

def handlers():
    bot.register_message_handler(get_info, commands=['start', 'help'], pass_bot=True)
    bot.register_message_handler(get_random_text, commands=['random'], pass_bot=True)
    bot.register_message_handler(get_random_text_mono, commands=['random_mono'], pass_bot=True)
    bot.register_inline_handler(inline_dispatch, lambda query: query, pass_bot=True)
    
handlers()

def run():
    bot.infinity_polling()

# Here we go !!!!!!!!
run()
