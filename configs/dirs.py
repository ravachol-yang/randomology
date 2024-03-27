# dir.py

import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
STORAGE_DIR = os.path.join(ROOT_DIR, "storage")
AUDIO_DIR = os.path.join(STORAGE_DIR, "audio")

PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
PUBLIC_STORAGE_DIR = os.path.join(PUBLIC_DIR, "storage")
PUBLIC_AUDIO_DIR = os.path.join(PUBLIC_STORAGE_DIR, "audio")
