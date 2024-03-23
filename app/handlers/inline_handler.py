# inline.py

from telebot import TeleBot
from telebot import types

from app.services.text_service import generate_random_text 

def inline_dispatch(inline_query, bot: TeleBot):
    try:
        text = types.InlineQueryResultArticle('1', 'Random Text',
                                              types.InputTextMessageContent(generate_random_text()))
        bot.answer_inline_query(inline_query.id, [text], cache_time=0)
    except Exception as e:
        print(e)
