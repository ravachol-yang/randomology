"""
voice.py
"""

import ffmpeg

from app.models.audio import Audio
from app.models.msg_type import MsgType

from configs import dirs

class Voice(Audio):

    MSG_TYPE:str = MsgType.VOICE

    def to_voice(self):
        wavfile = self._filepath
        oggfile_name = self._filename+".ogg"
        oggfile = dirs.AUDIO_DIR + oggfile_name
        (
            ffmpeg
            .input(wavfile, format="wav")
            .output(oggfile, acodec = "libopus")
            .run()
        )
        self._filename = oggfile_name
        self._filepath = dirs.AUDIO_DIR+self._filename
        self._content = Voice.HOST_PREFIX+"/storage/audio"+self._filename

        return self
