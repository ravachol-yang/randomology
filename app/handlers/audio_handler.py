# audio_handler.py

from telebot import TeleBot
from telebot.types import Message

from app.models.audio import Audio
from app.services.audio_service import generate_random_voice

# invoke with "/audio" command
def get_random_audio(message: Message, bot: TeleBot, data: dict):
    # pretend to be uploading audio
    bot.send_chat_action(message.chat.id, "upload_voice")
    options = data['options']

    audio = Audio(bot, message)
    audio.generate(options).to_mpeg.send()
    
# invoke with "/voice" command
def get_random_voice(message: Message, bot: TeleBot):
    # pretend to be sending voice
    bot.send_chat_action(message.chat.id, "record_voice")
    voice = generate_random_voice()
    bot.send_voice(message.chat.id, voice)
