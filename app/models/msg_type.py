"""
msg_type.py
enum for message types
""" 
from enum import Enum

class MsgType(str, Enum):
    TEXT:str = "message"
    AUDIO:str = "audio"
    VOICE:str = "voice"
