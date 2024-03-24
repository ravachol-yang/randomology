# audio_service

import wave
import random
import struct
import uuid
import ffmpeg

from configs import config

# Generate random audio in .wav
def generate_random_audio():
    # filename
    name = uuid.uuid4().hex
    audio_path = config.AUDIO_DIR+"/"+name+".wav"
    # open file in write mode
    audio = wave.open(audio_path, "wb")
    audio.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    values = []

    # length of the audio (in chunks)
    len = random.randint(20, 60)
    # generate the content of the audio
    for i in range(0, len):
        v1 = random.randint(-32768, 32768)
        v2 = random.randint(-32768, 32768)
        v1_packed = struct.pack('h', v1)
        v2_packed = struct.pack('h', v2)
        # chunk duration
        duration = random.randint(1000, 10000)
        for j in range(0, duration):
            values.append(v1_packed)
            values.append(v2_packed)
    # make a byte string
    values_str = b''.join(values)
    # write into the file
    audio.writeframes(values_str)
    # close
    audio.close()
    
    return open(audio_path, "rb")

# generate random voice in .ogg by converting .wav file
def generate_random_voice():
    # generate a random wav file
    wavfile = generate_random_audio()
    # file name of the generated .ogg
    oggfile = wavfile.name+".ogg"
    # convert with ffmpeg
    (
        ffmpeg
        .input(wavfile.name, format="wav")
        .output(oggfile, acodec = "libopus")
        .run()
    )

    return open(oggfile, "rb")
