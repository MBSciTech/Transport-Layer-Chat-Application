# protocol.py

def format_broadcast(username, message):
    return f"{username}: {message}"

def format_private(sender, message):
    return f"[PRIVATE] {sender}: {message}"

def is_private_message(message):
    return message.startswith("pvtmsg/")

def parse_private_message(message):
    # pvtmsg/UserB hi
    parts = message.split("/", 2)
    receiver = parts[1]
    msg = parts[2]
    return receiver, msg
