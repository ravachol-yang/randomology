# the randomology telegram bot

import logging

# config
from configs import env 

from routes import commands
from routes import handlers
import server

# pyTelegramBotAPI
import telebot

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# bot initialize 
bot = telebot.TeleBot(env.BOT_TOKEN)

# register commands
commands.register(bot)

# register handlers
handlers.register(bot)

# here we go !!!
if env.BOT_ENVIRONMENT == "prod":
    server.run(bot)
else:
    server.run_dev(bot)
