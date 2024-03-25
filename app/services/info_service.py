# info_service.py

from configs import templates

# generate info 
def generate_info(name, id):
    return templates.INFO_MESSAGE.format(name=name, id=id)
