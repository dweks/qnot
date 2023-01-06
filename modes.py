import tkinter as tk
from tkinter import ttk
from dispatch.adm import admin_dispatch
from dispatch.mod import mod_dispatch
from dispatch.std import std_dispatch
from ut.disp import warn, f, gry
from ut.debug import debug
from output import Output, Listing, Message
from exceptions import QnotException, InvalidInput, SelectBeforeModify, ListBeforeSelect
from carg import Carg

DEF_LAST = 5


class Standard:
    def __init__(self, carg: Carg):
        self.handle_output(std_dispatch[carg.c](carg.a))

    @staticmethod
    def handle_output(output):
        if output == "added":
            print("Note added.")


def mode_select(selection: Listing) -> bool:
    single: bool = True if selection.item_count == 1 else False
    show_list: bool = True
    done: bool = False
    end: bool = False

    def prompt() -> Carg:
        inp: list = input(gry("qnot") + f(">> ", 'lr', 'b')).split()
        return Carg(None if len(inp) == 0 else inp[0], None)

    def execute(carg: Carg) -> Output or None:
        if not carg.is_mod():
            if not carg.is_empty():
                return Message("context", f"{warn('Use mod commands or enter `x` to exit modify mode.')}")
        else:
            return mod_dispatch[carg.c](selection.items)

    def handle_output(output) -> bool:
        nonlocal done
        nonlocal end

        if output == "context":
            output.display()
        elif output == "revised":
            output.display()
            done = True
        elif output == "cancel":
            output.display()
            done = True
        elif output == "exported":
            output.display()
            done = True
        elif output == "next":
            return False if selection.next_page() is None else True
        elif output == "prev":
            return False if selection.prev_page() is None else True
        elif output == "exit":
            done = True
        elif output == "deleted":
            output.display()
            done = True
        elif output == "merged":
            output.display()
            done = True
        elif output == "quit":
            end = True
        return False

    # Interface
    while not done and not end:
        try:
            if show_list:
                if single:
                    selection.display(long=True)
                    print(f("(e)dit, (del)ete, (ex)port, or e(x)it", 'c'))
                else:
                    selection.display(tiny=True)
                    print(f("(del)ete, (m)erge, (ex)port, or e(x)it", 'c'))
            show_list = handle_output(execute(prompt()))
        except QnotException as e:
            print(e)
    return end


class Admin:
    def __init__(self, carg: Carg or None = None):
        self.root = tk.Tk()
        WW: int = 700
        WH: int = 600
        center_x = int(900 - WW / 2)
        center_y = int(500 - WH / 2)

        self.root.title("qnot")
        self.root.geometry(f"{WW}x{WH}+{center_x}+{center_y}")

        disp_frame = ttk.Frame(self.root, borderwidth=1, relief="solid")
        disp_frame.pack(padx=10, pady=10, anchor=tk.N, fill=tk.BOTH)
        disp_test = ttk.Label(disp_frame, text="disp_test", background="red")
        disp_test.pack(expand=True, fill=tk.BOTH)

        msg_frame = ttk.Frame(self.root, borderwidth=1, relief="solid")
        msg_frame.pack(padx=10, pady=10, expand=True, anchor=tk.S, fill=tk.X)
        msg_test = ttk.Label(msg_frame, text="msg_test", background="blue")
        msg_test.pack(expand=True, fill=tk.BOTH)

        inp_frame = ttk.Frame(self.root)
        inp_frame.pack(padx=10, pady=10, expand=True, anchor=tk.S, fill=tk.X)
        qnot_prompt = ttk.Label(inp_frame, text="qnot> ")
        qnot_prompt.pack(expand=False, side=tk.LEFT)

        self.inp = tk.StringVar()

        inp_entry = ttk.Entry(inp_frame, textvariable=self.inp)
        inp_entry.bind('<Return>', self.__execute)
        inp_entry.pack(fill=tk.X, expand=True)
        inp_entry.focus()

        self.done: bool = False
        self.view: Listing or None = None
        self.view_carg: Carg = Carg()
        self.root.mainloop()

    def interface(self):
        while not self.done:
            try:
                if isinstance(self.view, Listing) and self.show_list:
                    self.view.display()
                elif self.show_list:
                    print(warn("No notes to list; add note, or search for notes to list here."))

                carg: Carg = self.__prompt()
                self.show_list = self.__handle_output(carg)

            except Exception as e:
                print(e)
                self.output = None
                self.show_list = False
        self.show_list = False

    def __prompt(self) -> Carg:
        # done: bool = False
        # raw: list = []
        # while not done:
        #     raw = input(gry("qnot") + f("> ", 'c')).split()
        #     done = False if len(raw) == 0 else True
        # inp_len = len(raw)
        # return Carg(raw[0] if inp_len >= 1 else None, raw[1:] if inp_len > 1 else None)
        pass

    def __execute(self, event) -> Output:
        raw = self.inp.get()
        inp_len = len(raw)
        carg = Carg(raw[0] if inp_len >= 1 else None, raw[1:] if inp_len > 1 else None)
        if carg.is_adm():
            self.output = admin_dispatch[carg.c](carg.a)
        elif carg.is_mod():
            raise SelectBeforeModify("modify")
        elif carg.is_sel():
            if not isinstance(self.view, Listing):
                raise ListBeforeSelect()
            self.done = mode_select(Listing("Selection", self.view.retrieve(
                [carg.c]+[i for i in carg.a] if carg.a is not None else [carg.c]),
                pp=10
            ))
            self.output = Message("selectend", f"{warn('Leaving modify mode.')}")
        elif carg.is_empty():
            self.output = Message("hide")
        else:
            raise InvalidInput("admin prompt", carg.c + (' ' + ' '.join(carg.a) if carg.a is not None else ''))

    def __handle_output(self, carg):
        if isinstance(self.output, Listing):
            self.view = self.output
            self.view_carg = carg
            self.output = None
            return True
        elif self.output == "selectend":
            self.output.display()
            self.refresh()
        elif self.output == "nomatch":
            self.output.display()
        elif self.output == "added":
            self.output.display()
            self.refresh()
        elif self.output == "next":
            return False if self.view.next_page() is None else True
        elif self.output == "prev":
            return False if self.view.prev_page() is None else True
        elif self.output == "show":
            return True
        elif self.output == "imported":
            self.output.display()
        elif self.output == "cancel":
            self.output.display()
        elif self.output == "quit":
            self.done = True
        return False

    def refresh(self):
        self.view = None
        self.output = self.__execute(self.view_carg)
        if isinstance(self.output, Listing):
            self.view = self.output

    def __debug(self):
        debug(f"query: {self.view_carg}")
        debug(f"output: {self.output}")
        debug(f"listing: {self.view}")
        debug(f"suspend: {self.show_list}")
        debug(f"refresh: {self.refresh}")
        debug(f"done: {self.done}")
