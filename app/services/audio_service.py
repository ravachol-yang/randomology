# audio_service

import wave
import random
import struct
import uuid
import ffmpeg
import math

from configs import config

SAMPLE_RATE = 8000

# generate a noise sample
def noise_sample():
    sample = random.randint(-32768, 32767)
    sample_packed = struct.pack('h', sample)
    return sample_packed

# generate a sine wave sample
def sine_sample(freq, volume, x):
    value = volume * math.sin(2 * math.pi * freq * (x / SAMPLE_RATE))
    sample = int(value * 32767.0)
    return struct.pack('h', sample)

# Generate random audio in .wav
def generate_random_audio():
    # filename
    name = uuid.uuid4().hex
    audio_path = config.AUDIO_DIR+"/"+name+".wav"
    # open file in write mode
    audio = wave.open(audio_path, "wb")
    audio.setparams((2, 2, 24000, 0, 'NONE', 'not compressed'))

    values = []

    len = random.randint(8, 10)

    # generate a mix of sine wave and noise
    for i in range(0, len):
        # two channels
        freq_channel_1 = random.randint(20, 1000)
        freq_channel_2 = random.randint(20, 1000)
        # duration of every chunk in seconds
        chunk_duration = random.uniform(1, 2)
        # volume
        volume_channel_1 = random.uniform(0.5, 1.0)
        volume_channel_2 = random.uniform(0.5, 1.0)
        # build the chunk
        for x in range(0, 2 * SAMPLE_RATE):
            sine_channel_1 = sine_sample(freq_channel_1, volume_channel_1, x)
            sine_channel_2 = sine_sample(freq_channel_2, volume_channel_2, x)
            noise = noise_sample()
            # channel 1
            if random.choice([True, False]):
                values.append(sine_channel_1)
            else:
                values.append(noise)
            # channel 2
            if random.choice([True, False]):
                values.append(sine_channel_2)
            else:
                values.append(noise)

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
