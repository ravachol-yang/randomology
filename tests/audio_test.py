# audio tests

import io

from app.services.audio_service import generate_random_audio
from app.services.audio_service import generate_random_voice

def test_audio_generated():
    audio = generate_random_audio()
    assert isinstance(audio, io.BufferedIOBase)

def test_voice_generated():
    voice = generate_random_voice()
    assert isinstance(voice, io.BufferedIOBase)
