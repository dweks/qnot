from cmds.help import exec_help
from cmds.full import exec_full
from cmds.view import exec_view
from cmds.remove import exec_remove
from cmds.edit import exec_edit


class Command:
    __exec = {
        'f': exec_full,
        'e': exec_edit,
        'v': exec_view,
        'h': exec_help,
        'r': exec_remove,
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



