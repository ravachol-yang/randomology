# audio_handler.py

from telebot import TeleBot
from telebot.types import Message

from app.services.audio_service import generate_random_audio
from app.services.audio_service import generate_random_voice

# invoke with "/random_audio" command
def get_random_audio(message: Message, bot: TeleBot):
    # pretend to be uploading audio
    bot.send_chat_action(message.chat.id, "upload_voice")
    audio = generate_random_audio()
    bot.send_audio(message.chat.id, audio)

def get_random_voice(message: Message, bot: TeleBot):
    # pretend to be sending voice
    bot.send_chat_action(message.chat.id, "record_voice")
    voice = generate_random_voice()
    bot.send_voice(message.chat.id, voice)
