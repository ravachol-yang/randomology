# chat.py: chat routes

from telebot import TeleBot

# handlers
from app.handlers.info_handler import get_info
from app.handlers.text_handler import get_random_text
from app.handlers.text_handler import get_random_text_mono
from app.handlers.audio_handler import get_random_noise
from app.handlers.audio_handler import get_random_sine
from app.handlers.audio_handler import get_random_mix
from app.handlers.audio_handler import get_random_voice
from app.handlers.member_handler import get_welcome
from app.handlers.inline_handler import inline_dispatch

# register handlers in chats
def register(bot:TeleBot):
    bot.register_message_handler(get_info, commands=['start', 'help'], pass_bot=True)
    # random text
    bot.register_message_handler(get_random_text, commands=['text'], pass_bot=True)
    bot.register_message_handler(get_random_text_mono, commands=['mono'], pass_bot=True)
    # random audio
    bot.register_message_handler(get_random_noise, commands=['noise'], pass_bot=True)
    bot.register_message_handler(get_random_sine, commands=['sine'], pass_bot=True)
    bot.register_message_handler(get_random_mix, commands=['mix'], pass_bot=True)
    # random voice (a mix of noise and sine wave sent as voice)
    bot.register_message_handler(get_random_voice, commands=['voice'], pass_bot=True)
    # chat member change
    bot.register_message_handler(get_welcome, content_types=['new_chat_members'], pass_bot=True)
    # inline
    bot.register_inline_handler(inline_dispatch, lambda query: query, pass_bot=True)