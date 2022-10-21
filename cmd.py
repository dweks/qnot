import exec as E
from cmds.help import exec_help
# TODO make exec cmds their own file and import


class Command:
    __exec = {
        'f': E.exec_full,
        'e': E.exec_edit,
        'v': E.exec_view,
        'h': exec_help,
        'r': E.exec_remove,
    }

    def __init__(self, command, args=None):
        self.__cmd = command
        self.__args = args

    def execute(self):
        if self.__cmd not in self.__exec.keys():
            print(f"Invalid command: {self.__cmd}")
            return None
        return self.__exec[self.__cmd](self.__args)

    def print_command(self):
        print("Command: ", self.__cmd, " Args: ", self.__args)



