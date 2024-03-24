# config

# for getting environment variable
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
STORAGE_DIR = os.path.join(ROOT_DIR, "storage")
AUDIO_DIR = os.path.join(STORAGE_DIR, "audio")
