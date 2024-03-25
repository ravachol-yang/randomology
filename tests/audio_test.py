# audio tests

import io

from app.services.audio_service import generate_random_noise
from app.services.audio_service import generate_random_sine
from app.services.audio_service import generate_random_mix
from app.services.audio_service import generate_random_voice

def test_noise_generated():
    noise = generate_random_noise()
    assert isinstance(noise, io.BufferedIOBase)

def test_sine_generated():
    sine = generate_random_sine()
    assert isinstance(sine, io.BufferedIOBase)

def test_mix_generated():
    mix = generate_random_mix()
    assert isinstance(mix, io.BufferedIOBase)

def test_voice_generated():
    voice = generate_random_voice()
    assert isinstance(voice, io.BufferedIOBase)
