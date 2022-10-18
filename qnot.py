#!/usr/bin/env python3
import os
import sys
import file as f
from parse import parse_raw
from note import Note
from cmd import Command


def initialize():
    if not os.path.exists(f.ASSETS_PATH):
        print(f.ASSETS_PATH)
        os.mkdir(f.ASSETS_PATH)
    if not os.path.exists(f.TAGS_PATH):
        print(f.TAGS_PATH)
        file = open(f.TAGS_PATH, "x")
        file.close()
    if not os.path.exists(f.SETTINGS_PATH):
        print(f.SETTINGS_PATH)
        file = open(f.SETTINGS_PATH, "x")
        file.close()
    if not os.path.exists(f.LOOKUP_PATH):
        print(f.LOOKUP_PATH)
        file = open(f.LOOKUP_PATH, "x")
        file.close()
    if not os.path.exists(f.NOTES_PATH):
        os.mkdir(f.NOTES_PATH)


def main():
    initialize()
    parsed = parse_raw(sys.argv)

    if isinstance(parsed, Note):
        f.write(parsed)
    elif isinstance(parsed, Command):
        parsed.print_command()
        command = parsed.execute()
        if not command:
            print("no success")
    # TODO elif isinstance(parsed, Interface)
    # ...for when qnot launched without args


if __name__ == "__main__":
    main()
