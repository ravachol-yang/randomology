# audio tests

from app.models.audio import Audio

def test_audio_generated():
    audio = Audio()
    assert isinstance(audio.generate(), Audio)

def test_audio_noise():
    audio = Audio()
    assert isinstance(audio.generate(options = ['noise']), Audio)

def test_audio_mix():
    audio = Audio()
    assert isinstance(audio.generate(options = ['noise', 'sine']), Audio)

def test_audio_wrong_options():
    audio = Audio()
    assert isinstance(audio.generate(options = ['aa']), Audio)

def test_audio_empty_options():
    audio = Audio()
    assert isinstance(audio.generate(options = ['']), Audio)
