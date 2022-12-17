from dispatch import admin_dispatch as dispatch, mod_dispatch
from util import msg, lred_b, lyel, warn, debug, suc, cyan_b
from listing import Listing
from exceptions import InvalidInput, MatchNotFound


# The user interface for qnot. 'Admin mode' only instantiates implicitly.
# It cannot be called with a specific cmds.
# When a user enters certain qnot commands from the Linux cmds-line,
# they will open in admin mode. If a user executes qnot without any arguments,
# admin mode begins.
#
# In admin mode, the user may interact with the note system with
# more options entering commands from the provided prompt. Any editing
# or removing notes, managing tags, changing settings, or searching
# for notes is done here.
class Admin:
    # TODO change default startup execution
    def __init__(self, cmd="last", args=None):
        if args is None:
            args = ['5']
        self.selection = None
        self.done = False
        self.modify = False
        self.query = cmd, args
        self.suspend = False
        self.refresh = False

        try:
            self.output = self.__execute(cmd, args)
        except MatchNotFound:
            self.output = None
        self.listing = self.output if isinstance(self.output, Listing) else None

        self.interface()

    def interface(self):
        # self.__debug()
        if self.refresh:
            self.__refresh()
        if self.listing is not None and not self.suspend:
            self.listing.display_page()
        elif not self.suspend:
            print(warn("No notes to list; add note, or search for notes to list here."))
        try:
            cmd, args = self.__prompt()

            if cmd is None:
                # print("// cmd is None:", cmd)
                if self.modify:
                    print(warn("Modify cancelled, reselect to modify."))
                    self.modify = False
                self.suspend = True
                self.output = None

            elif cmd in dispatch.keys():
                # print("// admin dispatch:", cmd)
                if self.modify:
                    print(warn("Modify cancelled, reselect to modify."))
                    self.modify = False
                self.output = self.__execute(cmd, args)

            elif cmd in mod_dispatch.keys():
                # print("// mod dispatch:", cmd)
                self.output = self.__execute(cmd, self.selection)
                self.modify = False
                self.selection = None

            elif cmd.isdigit():
                # print("// is digit:", cmd)
                if self.modify:
                    print(warn("Modify cancelled, reselect to modify."))
                self.modify = True
                self.output = None
                self.selection = self.listing.retrieve(int(cmd))
                print(lyel(f"\nViewing {int(cmd)}"))
                self.selection.print_multiline()

            else:
                if self.modify:
                    print(warn("Modify cancelled, reselect to modify."))
                    self.modify = False
                self.suspend = True
                raise InvalidInput("admin prompt", cmd + (' ' + ' '.join(args) if args is not None else ''))

            self.suspend = True
            self.refresh = False
            self.__handle_output(cmd, args)

        except Exception as e:
            print(e)

        if self.done:
            return
        self.interface()

    def __prompt(self):
        cmd, args = None, None
        if self.modify:
            print(msg("Choose (e)dit or (r)emove\nLeave blank or call other command to cancel."))
            raw_input = input(cyan_b(">> ")).split()
        else:
            raw_input = input(cyan_b("> ")).split()
        if len(raw_input) >= 1:
            cmd = raw_input[0]
            if len(raw_input) > 1:
                args = raw_input[1:]
        return cmd, args

    def __execute(self, cmd, args):
        if self.modify:
            return mod_dispatch[cmd](args)
        return dispatch[cmd](args)

    def __handle_output(self, cmd, args):
        if isinstance(self.output, Listing):
            self.query = cmd, args
            self.listing = self.output
            self.suspend = False

        elif self.output == "deleted":
            print(suc("Note deleted."))
            self.refresh = True

        elif self.output == "added":
            print(suc("Note added."))
            self.refresh = True

        elif self.output == "cancel":
            print(warn("Nothing changed. Select again to modify."))
            self.suspend = False

        elif self.output == "next":
            if self.listing.next_page() is not None:
                self.suspend = False

        elif self.output == "prev":
            self.suspend = True
            if self.listing.prev_page() is not None:
                self.suspend = False

        elif self.output == "suspend":
            self.suspend = True

        elif self.output == "show":
            self.suspend = False

        elif self.output == "quit":
            self.done = True

        else:
            self.suspend = True

    def __refresh(self):
        ret = self.__execute(self.query[0], self.query[1])
        self.listing = ret if isinstance(ret, Listing) else None
        self.refresh = False

    def __debug(self):
        debug(f"query: {self.query}")
        debug(f"output: {self.output}")
        debug(f"selection: {self.selection}")
        debug(f"listing: {self.listing}")
        debug(f"modify: {self.modify}")
        debug(f"suspend: {self.suspend}")
        debug(f"refresh: {self.refresh}")
        debug(f"done: {self.done}")
