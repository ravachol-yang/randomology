# text_service.py

import random
import string

#  random text generater for the following handlers
def generate_random_text():
    length = random.randint(30,120)
    return ''.join(random.choices(string.ascii_letters +
                                  string.digits +
                                  string.punctuation, k=length))
