#!/usr/bin/env python3
from parse import initial_parse
from file import write
from action import Note
import sys


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


class Command:
    def __init__(self):
        pass

    def is_command(self, argv):
        pass


def main():
    # Some key in main that directs how argv is treated
    # either as note, command, error

    parsed = initial_parse(sys.argv)
    print(parsed)
    if isinstance(parsed, Note):
        write(parsed)
    elif isinstance(parsed, Command):
        pass


if __name__ == "__main__":
    main()
