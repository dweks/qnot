from edit import edit


class Command:
    valid_commands = ('f', 'e', 'v', 'h', 'r')
    valid_arguments = {
        'e': ["last"],
        'v': ["all", "recent", "today", "last", "tag", "title"],
        'h': ["view", "edit", "full", "tag", "title", "remove"],
        'r': ["last"]
    }

    def __init__(self, command, args=None):
        self.__command = command
        self.__args = args

    def execute(self):
        if not self.__validate_command():
            return None
        if self.__command == 'f':
            edit()

    def print_command(self):
        print("Command: ", self.__command, " Args: ", self.__args)

    def __validate_command(self):
        if self.__command not in self.valid_commands:
            return False
        if self.__args and self.__args[0] not in self.valid_arguments[self.__command]:
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
