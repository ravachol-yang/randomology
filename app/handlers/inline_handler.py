# inline.py

from telebot import TeleBot
from telebot import types

from app.models.text import Text
from app.models.voice import Voice

def inline_text(inline_query, bot: TeleBot, data:dict):
    options = data['options']
    text = Text()
    voice = Voice()
    try:
        text = types.InlineQueryResultArticle('2', 'Random Text',
                                              types.InputTextMessageContent(text.generate(options).content()))
        bot.answer_inline_query(inline_query.id, [text], cache_time=0)
    except Exception as e:
        print(e)

def inline_voice(inline_query, bot:TeleBot, data:dict):
    options = data['options']
    voice = Voice().generate(options).to_voice().content()
    try:
        voice = types.InlineQueryResultVoice('3', title = 'Random Voice',
                                             voice_url=voice)
        bot.answer_inline_query(inline_query.id, [voice], cache_time=0)
    except Exception as e:
        print(e)
