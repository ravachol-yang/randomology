# member_service.py

from configs import templates

# generate welcome message
def generate_welcome(name, id):
    return templates.WELCOME_MESSAGE.format(name=name, id=id)
