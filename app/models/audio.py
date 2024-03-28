"""
audio.py
the model for audio messages
"""
import wave
import random
import struct
import uuid
import math
import ffmpeg

from app.models.base import Base
from app.models.msg_type import MsgType

from configs import dirs
from configs import env

class Audio(Base):

    MSG_TYPE:str = MsgType.AUDIO

    HOST_PREFIX = "http://{}:{}".format(env.WEBHOOK_HOST, env.WEBHOOK_PORT)
    
    SAMPLE_RATE = 8000
    FREQ_HIGH = 800
    FREQ_LOW = 200
    VOLUME_HIGH = 0.6
    VOLUME_LOW = 0.3

    OPTIONS_AVAILABLE = ['sine', 'noise']
    OPTIONS_DEFAULT = {
        "sine": True,
        "noise": False
    }

    # generate a noise sample
    @staticmethod
    def noise_sample():
        sample = random.randint(-32768, 32767)
        sample_packed = struct.pack('h', sample)
        return sample_packed

    # generate a sine sample
    @staticmethod
    def sine_sample(freq, volume, x):
        value = volume * math.sin(2 * math.pi * freq * (x / Audio.SAMPLE_RATE))
        sample = int(value * 32767.0)
        return struct.pack('h', sample)

    # mix up according to options
    def _mix_up(self, len):
        values = []
        for i in range(0, len):
            if self._options['sine']:
                # two channels
                freq_channel_1 = random.randint(Audio.FREQ_LOW, Audio.FREQ_HIGH)
                freq_channel_2 = random.randint(Audio.FREQ_LOW, Audio.FREQ_HIGH)
                #volume
                volume_channel_1 = random.uniform(Audio.VOLUME_LOW, Audio.VOLUME_HIGH)
                volume_channel_2 = random.uniform(Audio.VOLUME_LOW, Audio.VOLUME_HIGH)
            # build the chunk
            # duration of every chunk
            chunk_duration = random.randint(1, 3)
            for x in range(0, chunk_duration * Audio.SAMPLE_RATE):
                if self._options['sine']:
                    sine_channel_1 = Audio.sine_sample(freq_channel_1, volume_channel_1, x)
                    sine_channel_2 = Audio.sine_sample(freq_channel_2, volume_channel_2, x)
                if self._options['noise']:
                    noise_channel_1 = Audio.noise_sample()
                    noise_channel_2 = Audio.noise_sample()

                # build into values
                if self._options['sine'] and self._options['noise']:
                    values.append(random.choice([sine_channel_1, noise_channel_1]))
                    values.append(random.choice([sine_channel_2, noise_channel_2]))
                elif self._options['sine'] and not self._options['noise']:
                    values.append(sine_channel_1)
                    values.append(sine_channel_2)
                elif self._options['noise'] and not self._options['sine']:
                    values.append(noise_channel_1)
                    values.append(noise_channel_2)
                 
        # make a byte string
        values_str = b''.join(values)
        return values_str
    
    # generate an audio
    def generate(self, options=None):
        name = uuid.uuid4().hex
        # add prefix to file name
        name_prefix = "/sine-"
        # set options
        self._options = dict(Audio.OPTIONS_DEFAULT)
        if options and not options == ['']:
            name_prefix = "/"
            self._options = dict.fromkeys(Audio.OPTIONS_AVAILABLE, False)
            for option in options:
                if option in Audio.OPTIONS_AVAILABLE:
                    self._options[option] = True
                    name_prefix = name_prefix + option + "-"

        # if options are empty now, return to default
        if self._options == dict.fromkeys(Audio.OPTIONS_AVAILABLE, False):
            self._options = dict(Audio.OPTIONS_DEFAULT)
            name_prefix += "sine-"
            
        self._filename = name_prefix+name+".wav"
        self._filepath = dirs.AUDIO_DIR+self._filename
        # open the audio file
        audio = wave.open(self._filepath, "wb")
        audio.setparams((2, 2, 24000, 0, 'NONE', 'not compressed'))

        # generate random length
        len = random.randint(8, 10)

        values_str = self._mix_up(len)

        audio.writeframes(values_str)
        audio.close()

        self._content = Audio.HOST_PREFIX+"/storage/audio"+self._filename
        print(self._content)
        
        return self

    # convert to mpeg for telegran server to download
    def to_mpeg(self):
        wavfile = self._filepath
        mpegfile = dirs.AUDIO_DIR+self._filename+".mp3"
        (
            ffmpeg
            .input(wavfile, format="wav")
            .output(mpegfile)
            .run()
        )
        self._filename = mpegfile
        self._filepath = dirs.AUDIO_DIR+self._filename
        self._content = Audio.HOST_PREFIX+"/storage/audio"+self._filename
        return self
