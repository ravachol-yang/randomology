# chat.py: chat routes

from telebot import TeleBot

# handlers
from app.handlers.info_handler import get_info
from app.handlers.text_handler import get_random_text
from app.handlers.text_handler import get_random_text_mono
from app.handlers.audio_handler import get_random_audio
from app.handlers.audio_handler import get_random_voice
from app.handlers.member_handler import get_welcome
from app.handlers.inline_handler import inline_text
from app.handlers.inline_handler import inline_voice

# register handlers in chats
def register(bot:TeleBot):
    bot.register_message_handler(get_info, commands=['start', 'help'], pass_bot=True)
    # random text
    bot.register_message_handler(get_random_text, commands=['text'], pass_bot=True)
    bot.register_message_handler(get_random_text_mono, commands=['mono'], pass_bot=True)
    # random audio
    bot.register_message_handler(get_random_audio, commands=['audio'], pass_bot=True)
    # random voice (a mix of noise and sine wave sent as voice)
    bot.register_message_handler(get_random_voice, commands=['voice'], pass_bot=True)
    # chat member change
    bot.register_message_handler(get_welcome, content_types=['new_chat_members'], pass_bot=True)
    # inline
    bot.register_inline_handler(inline_voice, lambda query: query.query.split(" ",1)[0] == "/v", pass_bot=True)
    bot.register_inline_handler(inline_text, lambda query: query or len(query.query) == 0, pass_bot=True)
