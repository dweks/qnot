#!/usr/bin/env python3
import os
import utilities as ut
import sys
from edit import handle_edit
from note import handle_note
from command import handle_command


def initialize():
    if not os.path.exists(ut.ASSETS_PATH):
        os.mkdir(ut.ASSETS_PATH)
    elif not os.path.exists(ut.TAGS_PATH):
        open(ut.TAGS_PATH, "w")
    elif not os.path.exists(ut.SETTINGS_PATH):
        open(ut.SETTINGS_PATH, "w")

    if not os.path.exists(ut.NOTES_PATH):
        os.mkdir(ut.NOTES_PATH)


def switch(argv):
    if len(argv) == 1:
        return "edit"
    else:
        if argv[1] in ('h', 'v', 'a'):
            return "command"
        else:
            return "note"


def main():
    initialize()
    mode = switch(sys.argv)

    if mode == "edit":
        handle_edit(None)
    if mode == "command":
        handle_command(sys.argv[1:])
    if mode == "note":
        handle_note(sys.argv[1:])


if __name__ == "__main__":
    main()
