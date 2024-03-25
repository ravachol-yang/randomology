# audio_handler.py

from telebot import TeleBot
from telebot.types import Message

from app.services.audio_service import generate_random_noise
from app.services.audio_service import generate_random_sine
from app.services.audio_service import generate_random_mix
from app.services.audio_service import generate_random_voice

# invoke with "/noise" command
def get_random_noise(message: Message, bot: TeleBot):
    # pretend to be uploading audio
    bot.send_chat_action(message.chat.id, "upload_voice")
    noise = generate_random_noise()
    bot.send_audio(message.chat.id, noise)

# invoke with "/sine" command
def get_random_sine(message: Message, bot: TeleBot):
    # uploading audio...
    bot.send_chat_action(message.chat.id, "upload_voice")
    sine = generate_random_sine()
    bot.send_audio(message.chat.id, sine)

# invoke with "/mix" command
def get_random_mix(message: Message, bot: TeleBot):
    # uploading audio...
    bot.send_chat_action(message.chat.id, "upload_voice")
    mix = generate_random_mix()
    bot.send_audio(message.chat.id, mix)
    
# invoke with "/voice" command
def get_random_voice(message: Message, bot: TeleBot):
    # pretend to be sending voice
    bot.send_chat_action(message.chat.id, "record_voice")
    voice = generate_random_voice()
    bot.send_voice(message.chat.id, voice)
