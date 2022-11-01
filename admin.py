from command import *
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
    dispatch = {
        None: exec_default,
        'quit': lambda x: "quit",
        'view': exec_view,
        'edit': exec_edit,
        'remove': exec_remove,
        'help': exec_help,
        'find': exec_find,
        'last': "_",
        'today': "_",
        'week': "_",
        'day': "_",
    }

    def __init__(self, cmd=None, args=None):
        # if cmd is None set self.output to default
        self.output = self.execute(cmd, args)
        self.interface(self.output)

    def interface(self, out=None):
        # have check for output being quit and then return

        if out == 'quit':
            return
        else:
            out.display()

        cmd, args = self.prompt()

        if cmd in self.dispatch.keys():
            out = self.execute(cmd, args)
            self.output = out

        return self.interface(out)

    @staticmethod
    def prompt():
        cmd, args = None, None
        raw_input = input("> ").split()
        if len(raw_input) >= 1:
            cmd = raw_input[0]
            if len(raw_input) > 1:
                args = raw_input[1:]

        return cmd, args

    def execute(self, cmd, args):
        print(cmd, args)
        return self.dispatch[cmd](args)
