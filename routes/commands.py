# commands.py: register commands

from telebot import TeleBot
from telebot import types

import telebot

def register(bot:TeleBot):
    bot.set_my_commands([
        telebot.types.BotCommand("help", "Get info"),
        telebot.types.BotCommand("text", "Random text"),
        telebot.types.BotCommand("mono", "Monospace random text"),
        telebot.types.BotCommand("audio", "Random audio"),
        telebot.types.BotCommand("voice", "Random voice")
    ])
