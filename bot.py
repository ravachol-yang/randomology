# the randomology telegram bot

# config
from configs import env 

from routes import commands
from routes import handlers

from configs import env

import server

from telebot import TeleBot

# pyTelegramBotAPI
import telebot

# bot initialize 
bot = telebot.TeleBot(env.BOT_TOKEN)

# register commands
commands.register(bot)

# register handlers
handlers.register(bot)

if env.BOT_ENVIRONMENT == "prod":
    server.run(bot)
else:
    server.run_dev(bot)
