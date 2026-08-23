import Commands as com
commands = {
    "info": com.information,
    "help": com.help_information,
    "echo" : com.echo,
    "cont" : com.countTo,
    "exit" : com.exit_shell,
    "calc" : com.calculator,
    "wsky" : com.build_wordskyscraper,


}

def get_command(command_name):
    if command_name in commands:
        return commands[command_name]
    else:
        return None
