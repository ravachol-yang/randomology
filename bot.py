# the randomology telegram bot

# config
from routes import commands
from routes import handlers
from app.middlewares.option_middleware import OptionMiddleware 

from configs import env

import server

from telebot import TeleBot

# pyTelegramBotAPI
import telebot

# bot initialize 
bot = telebot.TeleBot(env.BOT_TOKEN, use_class_middlewares=True)

# register commands
commands.register(bot)

# register handlers
handlers.register(bot)

# Setup middlewares
bot.setup_middleware(OptionMiddleware())

# here we go !!!
if env.BOT_ENVIRONMENT == "prod":
    server.run(bot)
else:
    server.run_dev(bot)
