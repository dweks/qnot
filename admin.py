from dispatch import admin_dispatch as dispatch
# TODO change this import to only import admin related commands
# TODO reorganize commands to have admin and basic


# The user interface for qnot. 'Admin mode' only instantiates implicitly.
# It cannot be called with a specific command.
# When a user enters certain qnot commands from the Linux command-line,
# they will open in admin mode. If a user executes qnot without any arguments,
# admin mode begins.
#
# In admin mode, the user may interact with the note system with
# more options entering commands from the provided prompt. Any editing
# or removing notes, managing tags, changing settings, or searching
# for notes is done here.
class Admin:
    def __init__(self, cmd=None, args=None):
        # if cmd is None set self.output to default
        self.output = self.__execute(cmd, args)
        self.interface()

    def interface(self):
        if self.output == 'quit':
            return
        elif self.output is not None:
            self.display()

        self.output = self.__prompt()
        return self.interface()

    def display(self):
        if type(self.output) is str:
            print(self.output)
        else:
            for page in self.output.pages:
                for note in self.output.pages[page]:
                    print(note.body)

    def __prompt(self):
        cmd, args = None, None
        raw_input = input("> ").split()
        if len(raw_input) >= 1:
            cmd = raw_input[0]
            if len(raw_input) > 1:
                args = raw_input[1:]

        if cmd in dispatch.keys():
            return self.__execute(cmd, args)
        else:
            return f"Unrecognized command '{cmd}'"

    @staticmethod
    def __execute(cmd, args):
        return dispatch[cmd](args)
