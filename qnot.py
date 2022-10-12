#!/usr/bin/env python3
import sys
from parse import parse_note, parse_command
from edit import handle_edit
from note import handle_note
from command import handle_command


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


COMMANDS = ('h', 'v', 'a')


def switch(argv):
    if len(argv) == 1:
        return "edit"
    else:
        if argv[1] in COMMANDS:
            return "command"
        else:
            return "note"


def main():
    mode = switch(sys.argv)
    result = None

    if mode == "edit":
        result = handle_edit()
    if mode == "command":
        result = handle_command(sys.argv[1:])
    if mode == "note":
        result = handle_note(sys.argv[1:])



if __name__ == "__main__":
    main()
