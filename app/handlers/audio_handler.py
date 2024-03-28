# audio_handler.py

from telebot import TeleBot
from telebot.types import Message

from app.models.audio import Audio
from app.models.voice import Voice

# invoke with "/audio" command
def get_random_audio(message: Message, bot: TeleBot, data: dict):
    # pretend to be uploading audio
    bot.send_chat_action(message.chat.id, "upload_voice")
    options = data['options']

    audio = Audio(bot, message)
    audio.generate(options).to_mpeg().send()
    
# invoke with "/voice" command
def get_random_voice(message: Message, bot: TeleBot, data: dict):
    # pretend to be sending voice
    bot.send_chat_action(message.chat.id, "record_voice")
    options = data['options']
    
    voice = Voice(bot, message)
    voice.generate(options).to_voice().send()
