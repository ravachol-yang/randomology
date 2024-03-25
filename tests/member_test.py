# member tests

from app.services.member_service import generate_welcome
from configs import templates

def test_welcome_template():
    assert isinstance(templates.WELCOME_MESSAGE, str)

def test_welcome_generated():
    welcome = generate_welcome("test",111)
    assert isinstance(welcome, str)
