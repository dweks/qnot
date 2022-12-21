from note import Note
from dispatch.adm import admin_dispatch
from dispatch.mod import mod_dispatch
from dispatch.std import std_dispatch
from ut.disp import msg, lred_b, lyel, warn, debug, suc, gray
from listing import Output, Listing, Message
from exceptions import InvalidInput, SelectBeforeModify, ListBeforeSelect
from carg import Carg

DEF_LAST = 5


# The user interface for qnot. 'Admin mode' only instantiates implicitly.
# It cannot be called with a specific carg.cs.
# When a user enters certain qnot commands from the Linux carg.cs-line,
# they will open in admin mode. If a user executes qnot without any arguments,
# admin mode begins.
#
# In admin mode, the user may interact with the note system with
# more options entering commands from the provided prompt. Any editing
# or removing notes, managing tags, changing settings, or searching
# for notes is done here.
class Admin:
    def __init__(self, carg: Carg or None = None):
        self.selection: Note or None = None
        self.done: bool = False
        self.modify: bool = False
        self.suspend: bool = False
        self.listing: Listing or None = None
        self.listing_carg: Carg or None = None
        self.out: Output or None = self.execute(carg)
        if type(self.out) is Listing:
            self.listing = self.out
            self.listing_carg = carg
        self.interface()

    def interface(self):
        try:
            if isinstance(self.listing, Listing) and not self.suspend:
                self.listing.display_page()
            elif not self.suspend:
                print(warn("No notes to list; add note, or search for notes to list here."))

            carg: Carg = self.prompt()
            self.out = self.execute(carg)
            self.suspend = self.handle_output(carg)

        except Exception as e:
            self.modify = False
            self.out = None
            self.selection = None
            self.suspend = True
            print(e)

        if self.done:
            return
        self.interface()

    def prompt(self) -> Carg:
        carg: Carg = Carg(None, None)
        p: str = gray("qnot") + lred_b("> ")
        if self.modify:
            print(msg(f"Choose (e)dit, (d)elete, or (ex)port\nLeave blank or call other command to cancel."))
            p = gray("qnot") + lred_b(">> ")
        raw_input: list[str] = input(p).split()
        if len(raw_input) >= 1:
            carg.c = raw_input[0]
            if len(raw_input) > 1:
                carg.a = raw_input[1:]
        return carg

    def execute(self, carg: Carg) -> Output or None:
        if not carg.is_mod() and self.modify:
            print(warn("Modify cancelled, reselect to modify."))
            self.modify = False
            self.selection = None
        if carg.is_none():
            return None
        elif carg.is_adm():
            return admin_dispatch[carg.c](carg.a)
        elif carg.is_mod():
            if not self.modify:
                raise SelectBeforeModify("modify")
            else:
                return mod_dispatch[carg.c](self.selection)
        elif carg.is_sel():
            self.modify = True
            if not isinstance(self.listing, Listing):
                raise ListBeforeSelect()
            self.selection = self.listing.retrieve(int(carg.c))
            # todo this heading needs to be dynamic when range select is implemented
            print(lyel(f"\nViewing {int(carg.c)}"))
            self.selection.print_full()
            return Message("selection", "admin execute")
        else:
            raise InvalidInput("admin prompt", carg.c + (' ' + ' '.join(carg.a) if carg.a is not None else ''))

    def handle_output(self, carg):
        if isinstance(self.out, Listing):
            self.listing = self.out
            self.listing_carg = carg
            self.out = None
            return False
        elif self.out == "deleted":
            self.modify = False
            print(suc("Note deleted."))
            self.refresh()
            return True
        elif self.out == "added":
            self.modify = False
            print(suc("Note added."))
            self.refresh()
            return True
        elif self.out == "revised":
            self.modify = False
            print(suc("Revisions saved."))
            self.refresh()
            return True
        elif self.out == "exported":
            self.modify = False
            print(suc(f"Note exported."))
            self.refresh()
            return True
        elif self.out == "cancel":
            print(warn("Nothing changed."))
            return True
        elif self.out == "next":
            if self.listing.next_page() is not None:
                return False
            return True
        elif self.out == "prev":
            if self.listing.prev_page() is not None:
                self.suspend = False
            return True
        elif self.out == "suspend":
            return True
        elif self.out == "show":
            return False
        elif self.out == "quit":
            self.done = True
            return True
        else:
            return True

    def refresh(self):
        self.listing = None
        self.out = self.execute(self.listing_carg)
        if isinstance(self.out, Listing):
            self.listing = self.out

    def __debug(self):
        debug(f"query: {self.listing_carg}")
        debug(f"output: {self.out}")
        debug(f"selection: {self.selection}")
        debug(f"listing: {self.listing}")
        debug(f"modify: {self.modify}")
        debug(f"suspend: {self.suspend}")
        debug(f"refresh: {self.refresh}")
        debug(f"done: {self.done}")


class Standard:
    def __init__(self, carg: Carg):
        std_dispatch[carg.c](carg.a)
