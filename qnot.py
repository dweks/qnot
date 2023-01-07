#!/usr/bin/env python3
from dispatch.adm import admin_dispatch
from dispatch.mod import mod_dispatch
from dispatch.std import std_dispatch
from output import Output, Listing, Message
from exceptions import QnotException, InvalidInput, SelectBeforeModify, ListBeforeSelect
from carg import Carg
import tkinter as tk
from tkinter import ttk
from db_access import db_init

DEF_LAST = "10"

WW: int = 700
WH: int = 600
center_x = int(900 - WW / 2)
center_y = int(500 - WH / 2)


def main():
    db_init()
    root = tk.Tk()
    root.title("qnot")
    root.geometry(f"{WW}x{WH}+{center_x}+{center_y}")

    inp = tk.StringVar()
    msg_var = tk.StringVar()

    def populate_disp(listing):
        for item in listing.items:
            ttk.LabelFrame(disp_frame, text=item.title).pack(anchor=tk.NW)

    def execute(event=None):
        nonlocal msg_var, inp
        raw = inp.get().split(' ')
        inp.set("")
        inp_len = len(raw)
        carg = Carg(raw[0] if inp_len >= 1 else None, raw[1:] if inp_len > 1 else None)
        try:
            output = admin_dispatch[carg.c](carg.a)
            if isinstance(output, Message):
                msg_var.set(output.body)
            elif isinstance(output, Listing):
                populate_disp(output)
        except Exception as e:
            msg_var.set(str(e))

    disp_frame = ttk.Frame(root, borderwidth=1, relief="solid", height=400)
    disp_frame.pack(padx=5, pady=5, anchor=tk.N, fill=tk.X)

    msg_frame = ttk.Frame(root, borderwidth=1, relief="solid")
    msg_frame.pack(padx=5, pady=5, expand=True, anchor=tk.S, fill=tk.BOTH)
    msg_label = ttk.Label(msg_frame, textvariable=msg_var)
    msg_label.pack(anchor=tk.NW, fill=tk.X)

    inp_frame = ttk.Frame(root)
    inp_frame.pack(padx=15, pady=15, expand=True, anchor=tk.S, fill=tk.X)

    qnot_prompt = ttk.Label(inp_frame, text="qnot> ")
    qnot_prompt.pack(expand=False, side=tk.LEFT)

    inp_entry = ttk.Entry(inp_frame, textvariable=inp)
    inp_entry.bind('<Return>', execute)
    inp_entry.pack(fill=tk.X, expand=True)
    inp_entry.focus()

    root.mainloop()


if __name__ == "__main__":
    main()
