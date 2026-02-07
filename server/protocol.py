def is_private_message(msg):
    return msg.startswith("pvtmsg/")

def parse_private_message(msg):
    """
    Format:
    pvtmsg/username message with spaces allowed
    """
    try:
        header, message = msg.split(" ", 1)  # ONLY ONE split
        _, receiver = header.split("/", 1)
        return receiver, message
    except ValueError:
        return None, None

def format_private(sender, msg):
    return f"[PRIVATE] {sender}: {msg}"

def format_broadcast(sender, msg):
    return f"{sender}: {msg}"
