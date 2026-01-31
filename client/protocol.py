def is_private_command(message):
    return message.startswith("pvtmsg/")

def help_message():
    return (
        "Commands:\n"
        "pvtmsg/username message  -> private message\n"
        "exit                     -> leave chat\n"
    )
