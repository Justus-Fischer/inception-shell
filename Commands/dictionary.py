commands = {
    "info": "information",
    "help": "help_information",


}

def get_command(command_name):
    if command_name in commands:
        return commands[command_name]
    else:
        return None
