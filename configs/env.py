# config
from configs.config_utils import env

# the bot token from telegran bot father
BOT_TOKEN = env(section = "bot",
                key = "token",
                default="")

# the bot name
BOT_NAME = env(section = "bot",
               key = "name",
               default = "randomology")

# environment, dev or prod
BOT_ENVIRONMENT = env(section = "bot",
                      key = "environment",
                      default="prod")

# your host
SERVER_HOST = env(section = "server",
                  key = "host",
                  default = "")

# port, default 443
SERVER_PORT = env(section = "server",
                  key = "port",
                  default = "443")

# some vps need this, default 0.0.0.0
SERVER_LISTEN = env(section = "server",
                    key = "listen",
                    default = "0.0.0.0")

# path to your ssl cert file
SSL_CERT = env(section = "ssl",
               key = "cert",
               default = "")

# path to your ssl private key
SSL_PRIV = env(section = "ssl",
               key = "priv",
               default = "")
