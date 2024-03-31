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

    # Stands for zh, english, punctuations, digits, must be in order
    OPTIONS_AVAILABLE = ['z', 'e', 'p','d']
    # Default: 0111
    OPTIONS_DEFAULT = {
        "z":{"enabled": False,
             "content": lambda zh:[zh+chr(random.randint(0x4e00,0xa000)) for i in range(0,30)]},
        "e":{"enabled": True,
             "content": string.ascii_letters},
        "p":{"enabled": True,
             "content": string.punctuation},
        "d":{"enabled": True,
             "content": string.digits}
    }
    
    # generate random string, returns the object itself
    def generate(self, options = None):
        # check options
        if options:
            self.set_options(options)
        
        # build the choices string
        choices_string = ""
        for i in self._options:
            if self._options[i]["enabled"]:
                # if the content is a function
                if callable(self._options[i]["content"]):
                    choices_string += "".join(self._options[i]["content"](""))
                else:
                    choices_string += "".join(self._options[i]["content"])
                    
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
        if self._options["p"]["enabled"]:
            # add a "\" before every special char 
            for i in Text.SPECIAL:
                self._content = self._content.replace(i,"\\"+i)
        # add ` ` around to parse to mono
        self._content = "` "+self._content+" `"
        return self
        
