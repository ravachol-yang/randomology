# the randomology telegram bot

# config
from configs import config

# handlers
from app.handlers.info_handler import get_info
from app.handlers.text_handler import get_random_text
from app.handlers.text_handler import get_random_text_mono
from app.handlers.audio_handler import get_random_audio
from app.handlers.audio_handler import get_random_voice
from app.handlers.inline_handler import inline_dispatch

# pyTelegramBotAPI
import telebot
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)

def commands():
    bot.set_my_commands([
        telebot.types.BotCommand("help", "Get info"),
        telebot.types.BotCommand("random", "Random text"),
        telebot.types.BotCommand("random_mono", "Monospace random text"),
        telebot.types.BotCommand("random_audio", "Random audio"),
        telebot.types.BotCommand("random_voice", "Random voice")
    ])

commands()

def handlers():
    # info
    bot.register_message_handler(get_info, commands=['start', 'help'], pass_bot=True)
    # random text
    bot.register_message_handler(get_random_text, commands=['random'], pass_bot=True)
    bot.register_message_handler(get_random_text_mono, commands=['random_mono'], pass_bot=True)
    # random audio
    bot.register_message_handler(get_random_audio, commands=['random_audio'], pass_bot=True)
    # random voice
    bot.register_message_handler(get_random_voice, commands=['random_voice'], pass_bot=True)
    # inline
    bot.register_inline_handler(inline_dispatch, lambda query: query, pass_bot=True)
    
handlers()

def run():
    bot.infinity_polling()

# Here we go !!!!!!!!
run()
