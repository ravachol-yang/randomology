# voice tests

from app.models.voice import Voice

def test_voice_generated():
    voice = Voice()
    assert isinstance(voice.generate().to_voice(), Voice)

def test_voice_noise():
    voice = Voice()
    assert isinstance(voice.generate(options = ['noise']).to_voice(), Voice)
