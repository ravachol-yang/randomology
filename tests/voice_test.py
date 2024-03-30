# voice tests

from app.models.voice import Voice

def test_voice_generated():
    voice = Voice()
    assert isinstance(voice.generate().to_voice(), Voice)

def test_voice_noise():
    voice = Voice()
    assert isinstance(voice.generate(options = {"bool_options":True, "options": [False, True]}).to_voice(), Voice)
