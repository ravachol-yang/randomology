# dir.py

import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
STORAGE_DIR = os.path.join(ROOT_DIR, "storage")
AUDIO_DIR = os.path.join(STORAGE_DIR, "audio")