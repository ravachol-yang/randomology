# info_test.py

from app.services.info_service import generate_info
from configs import templates

def test_welcome_template():
    assert isinstance(templates.INFO_MESSAGE, str)

def test_info_generated():
    info = generate_info("test", 111)
    assert isinstance(info, str)
