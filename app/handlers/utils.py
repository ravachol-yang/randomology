# utils.py

def get_options(message_text:str, remove_cmd:bool):
    # remove command from message content
    if remove_cmd:
        options = message_text.split(" ",1)
        options.pop(0)
    else:
        options = [message_text]

    if options:
        # remove spaces and make options list
        options = options[0].replace(" ","")
        options = options.split(",")

    return options
    
