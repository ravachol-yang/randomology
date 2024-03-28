"""
audio.py
the model for audio messages
""" 
from app.models.base import Base
from app.models.msg_type import MsgType

class Audio(Base):

    MSG_TYPE:str = MsgType.AUDIO

    def generate(self):
        pass
