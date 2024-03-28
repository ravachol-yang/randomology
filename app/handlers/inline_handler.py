# inline.py

from telebot import TeleBot
from telebot import types

from app.models.text import Text
from app.models.voice import Voice

def inline_dispatch(inline_query, bot: TeleBot, data:dict):
    options = data['options']
    text = Text()
    voice = Voice().generate(options).content()
    try:
        text = types.InlineQueryResultArticle('1', 'Random Text',
                                              types.InputTextMessageContent(text.generate(options).content()))
        voice = types.InlineQueryResultVoice('2', caption = 'Random Voice',
                                             voice_url=voice)
        bot.answer_inline_query(inline_query.id, [text, voice], cache_time=0)
    except Exception as e:
        print(e)
