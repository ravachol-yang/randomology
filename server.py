# server.py

import fastapi
import uvicorn

from configs import env

from telebot import TeleBot

TOKEN = env.BOT_TOKEN

HOST = env.SERVER_HOST
PORT = env.SERVER_PORT
LISTEN = env.SERVER_LISTEN

SSL_CERT = env.SSL_CERT
SSL_PRIV = env.SSL_PRIV

URL_BASE = "https://{}:{}".format(HOST, PORT)
URL_PATH = "/bot{}/".format(TOKEN)

# when in production
def run(bot:TeleBot):
    # create the app
    app = fastapi.FastAPI(docs=None, redoc_url=None)

    @app.post(f'/bot{TOKEN}/')
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

# when in dev environment 
def run_dev(bot:TeleBot):
    bot.infinity_polling()
