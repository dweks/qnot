from cmds.edit import cmd_full, cmd_edit
from cmds.help import cmd_help
from cmds.view import cmd_view
from cmds.remove import cmd_remove


class Command:
    __exec = {
        'f': (cmd_full, None),
        'e': (cmd_edit, {"last"}),
        'v': (cmd_view, {"all", "recent", "today", "last", "tag", "title"}),
        'h': (cmd_help, {"view", "edit", "full", "tag", "title", "remove"}),
        'r': (cmd_remove, {"last"})
    }

    def __init__(self, command, args=None):
        self.__cmd = command
        self.__args = args

    def execute(self):
        if not self.__validate_command():
            return None
        return self.__exec[self.__cmd][0](self.__cmd, self.__args)

    def print_command(self):
        print("Command: ", self.__cmd, " Args: ", self.__args)

    def __validate_command(self):
        if self.__cmd not in self.__exec:
            return False
        if self.__args and self.__args[0] not in self.__exec[self.__cmd][1]:
            return False
        return True


class Help:
    @staticmethod
    def basic_instructions():
        print("Basic Usage:")
        print()
        print("(1) Create new note (with title):")
        print("    qnot some title :: note with +tags")
        print()
        print("(2) Create new note (without title):")
        print("    qnot note with +tags")
        print()
        print("(3) View note (interface)")
        print("    qnot view")
        print()
        print("(4) View note (with arguments)")
        print("    qnot view <argument>")
        print()
        print("(5) Detailed help")
        print("    qnot help <argument>")
        print("    NOTE: Replace <argument> with command:")
        print("       view, help, edit, remove, tags")
