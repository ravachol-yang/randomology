# text tests

from app.services.text_service import generate_random_text

def test_text_generated():
    text = generate_random_text()
    assert isinstance(text, str)

def test_text_length():
    text = generate_random_text()
    assert len(text) >= 30 and len(text) <= 120
