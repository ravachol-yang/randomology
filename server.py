# server.py

import fastapi
import uvicorn
import telebot

from configs import env

from telebot import TeleBot

BOT_NAME = env.BOT_NAME

SERVER_HOST = env.SERVER_HOST
SERVER_PORT = env.SERVER_PORT
SERVER_LISTEN = env.SERVER_LISTEN

WEBHOOK_HOST = env.WEBHOOK_HOST
WEBHOOK_PORT = env.WEBHOOK_PORT

SSL_CERT = env.SSL_CERT
SSL_PRIV = env.SSL_PRIV

URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
URL_PATH = "/{}/".format(BOT_NAME)

# when in production
def run(bot:TeleBot):
    # create the app
    app = fastapi.FastAPI(docs=None, redoc_url=None)

    @app.post(f'/{BOT_NAME}/')
    def process_webhook(update:dict):
        if update:
            update = telebot.types.Update.de_json(update)
            bot.process_new_updates([update])
        else:
            return
               
    # remove previous webhook(?)
    bot.remove_webhook()

    # set webhook
    bot.set_webhook(
        url=URL_BASE+URL_PATH
    )
    
    # run the server
    uvicorn.run(
        app,
        host=SERVER_HOST,
        port=SERVER_PORT,
        ssl_certfile=SSL_CERT,
        ssl_keyfile=SSL_PRIV
    )

# when in dev environment 
def run_dev(bot:TeleBot):
    bot.infinity_polling()
