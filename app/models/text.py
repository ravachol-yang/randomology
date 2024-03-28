"""
text.py
the model for text messages
"""

import random
import string

from app.models.base import Base
from app.models.msg_type import MsgType

class Text(Base):

    # type of this object ("message")
    MSG_TYPE:str = MsgType.TEXT

    # special chars to be backslashed in mono
    SPECIAL = ['_', '*', '[', ']',
               '(', ')', '~', '`',
               '<', '>', '#', '+',
               '-', '=', '|', '{',
               '}', '.', '!']
    
    OPTIONS_AVAILABLE = ['en', 'zh', 'punc','d']
    OPTIONS_DEFAULT = {
        "en": True,
        "zh": False,
        "punc": True,
        "d": True,
    }

    # set content
    def set_content(self, text:str):
        self._content = text
        return self
    
    # generate random string, returns the object itself
    def generate(self, options = None):

        # set default options
        self._options = dict(self.OPTIONS_DEFAULT)
        
        # if option not nothing
        if options:
            option_bodies = []
            # check each option in options
            for option in options:
                # if the option is empty, we see it as setting all others false
                if option == '':
                    for i in self.OPTIONS_AVAILABLE:
                        if i not in option_bodies:
                            self._options[i] = False
                # if the option is not empty
                else:
                    # get option body without "+" or "-"
                    if option[0] == "+" or option[0] == "-":
                        option_body = option.replace(option[0],"",1)
                        option_bodies.append(option_body)
                    else:
                        # if option has no operator, it is "+"
                        option_body = option
                        option_bodies.append(option_body)
                    if option_body in self.OPTIONS_AVAILABLE:
                        if option[0] == '-':
                            self._options[option_body] = False
                        else:
                            self._options[option_body] = True

        # make choice string
        choices_string = ""

        # add strings for each options
        if self._options["en"]:
            choices_string += string.ascii_letters

        if self._options["zh"]:
            zh_string = ""
            # generate a Chinese string of 30 chars
            for i in range(0,30):
                zh_string += chr(random.randint(0x4e00, 0xa000))
            choices_string += zh_string
        
        if self._options["punc"]:
            choices_string += string.punctuation

        if self._options["d"]:
            choices_string += string.digits

        # if the string is empty, return random *s
        if not choices_string:
            choices_string = "*"

        # generate random string
        length = random.randint(30,120)
        self._content = ''.join(random.choices(choices_string, k = length))
        
        return self

    # convert to mono for markdown parsing
    def to_mono(self):
        # if there is no puncs, no need to check
        if self._options['punc']:
            # add a "\" before every special char 
            for i in self.SPECIAL:
                self._content = self._content.replace(i,"\\"+i)
        # add ` ` around to parse to mono
        self._content = "` "+self._content+" `"
        return self
        
