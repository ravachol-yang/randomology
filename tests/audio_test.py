# audio tests

from app.models.audio import Audio

def test_audio_generated():
    audio = Audio()
    assert isinstance(audio.generate(), Audio)

def test_audio_noise():
    audio = Audio()
    assert isinstance(audio.generate(options = {"bool_options": True, "options":[False,True]}), Audio)

def test_audio_mix():
    audio = Audio()
    assert isinstance(audio.generate(options = {"bool_options": True, "options":[True,True]}), Audio)

def test_audio_empty_options():
    audio = Audio()
    assert isinstance(audio.generate(options = {"bool_options": False, "options": "aa"}), Audio)

def test_audio_to_mpeg():
    audio = Audio()
    audio.generate()
    mpeg = audio.to_mpeg()
    assert isinstance(mpeg, Audio)
