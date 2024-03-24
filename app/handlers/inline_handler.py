# inline.py

from telebot import TeleBot
from telebot import types

from app.services.text_service import generate_random_text
from app.services.audio_service import generate_random_audio

def inline_dispatch(inline_query, bot: TeleBot):
    try:
        text = types.InlineQueryResultArticle('1', 'Random Text',
                                              types.InputTextMessageContent(generate_random_text()))
        audio = types.InlineQueryResultArticle('2',
                                               'TODO',
                                               types.InputTextMessageContent("TODO"))
        bot.answer_inline_query(inline_query.id, [text, audio], cache_time=0)
    except Exception as e:
        print(e)
