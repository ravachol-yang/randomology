# text tests

from app.models.text import Text
from configs import templates

def test_text_generated():
    text = Text()
    assert isinstance(text.generate().content(),str)

def test_text_options():
    text = Text()
    text.generate(options = {"bool_options":True, "options":[True, True, True, False]})
    assert isinstance(text.content(),str)

def test_text_option_only():
    text = Text()
    text.generate(options = {"bool_options":True, "options":[False, False, False, True]})
    assert isinstance(text.content(),str) and text.content().isdigit()

def test_text_wrong_options():
    text = Text()
    text.generate(options = {"bool_options": True, "options":[True,False,True,False,False]})
    assert isinstance(text.content(),str) and text.content().isascii()

def test_text_empty_options():
    text = Text()
    text.generate(options = {"bool_options": False, "options": "aaa"})
    assert isinstance(text.content(),str) and text.content().isascii()
    

def test_text_mono():
    text = Text()
    text.generate()
    text.to_mono()
    assert isinstance(text.content(),str) and (text.content()[0]=="`") and (text.content()[-1]=="`")

def test_get_welcome():
    welcome = templates.WELCOME_MESSAGE
    assert isinstance(welcome, str)

def test_get_info():
    info = templates.INFO_MESSAGE
    assert isinstance(info, str)
