#!/usr/bin/env python3
import os
import sys
import file as f
from database.db import db_init
from parse import parse_raw
from note import Note
from cmd import Command


def initialize():
    if not os.path.exists(f.DB_PATH):
        os.mkdir(f.DB_PATH)
    db_init()

    # Below: json stuff
    if not os.path.exists(f.ASSETS_PATH):
        os.mkdir(f.ASSETS_PATH)
    if not os.path.exists(f.TAGS_PATH):
        file = open(f.TAGS_PATH, "x")
        file.close()
    if not os.path.exists(f.SETTINGS_PATH):
        file = open(f.SETTINGS_PATH, "x")
        file.close()


def main():
    initialize()
    parsed = parse_raw(sys.argv)

    if isinstance(parsed, Note):
        print("[ NOTE ]")
        parsed.debug_print()
        f.write(parsed)
    elif isinstance(parsed, Command):
        print("[ COMMAND ]")
        parsed.print_command()
        command = parsed.execute()
    # TODO elif isinstance(parsed, Interface)
    # ...for when qnot launched without args


if __name__ == "__main__":
    main()
