# inline.py

from telebot import TeleBot
from telebot import types

from app.models.text import Text

def inline_dispatch(inline_query, bot: TeleBot, data:dict):
    options = data['options']
    if options == ['']:
        options = None
    text = Text()
    try:
        text = types.InlineQueryResultArticle('1', 'Random Text',
                                              types.InputTextMessageContent(text.generate(options).content()))
        audio = types.InlineQueryResultArticle('2',
                                               'TODO',
                                               types.InputTextMessageContent("TODO"))
        bot.answer_inline_query(inline_query.id, [text, audio], cache_time=0)
    except Exception as e:
        print(e)
