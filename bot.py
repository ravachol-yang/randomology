# the randomology telegram bot

# config
from configs import env 

from routes import commands
from routes import handlers

import fastapi
import uvicorn
import telebot

from configs import env

from telebot import TeleBot

# pyTelegramBotAPI
import telebot

# bot initialize 
bot = telebot.TeleBot(env.BOT_TOKEN)

# register commands
commands.register(bot)

# register handlers
handlers.register(bot)

TOKEN = env.BOT_TOKEN

HOST = env.SERVER_HOST
PORT = env.SERVER_PORT
LISTEN = env.SERVER_LISTEN

SSL_CERT = env.SSL_CERT
SSL_PRIV = env.SSL_PRIV

URL_BASE = "https://{}:{}".format(HOST, PORT)
URL_PATH = "/{}/".format(TOKEN)

app = fastapi.FastAPI(docs=None, redoc_url=None)

@app.post(f'/{TOKEN}/')
def process_webhook(update:dict):
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_pupdates([update])
    else:
        return

# remove previous webhook(?)
bot.remove_webhook()

# set webhook
bot.set_webhook(
    url=URL_BASE+URL_PATH,
    certificate=open(SSL_CERT, 'r')
)

# run the server
uvicorn.run(
    app,
    host=HOST,
    port=PORT,
    ssl_certfile=SSL_CERT,
    ssl_keyfile=SSL_PRIV
)

