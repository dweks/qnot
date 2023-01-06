#!/usr/bin/env python3
import sys
import re
from db_access import db_init
from modes import Admin, Standard
from carg import Carg
from exceptions import NoSuchCommand

DEF_LAST = "10"


# The router determines the correct context for execution of commands from
# cmd_accessories-line arguments. If the router detects a cmd_accessories in the input (if the
# first argument begins with a `-`) it will verify which context the cmd_accessories
# belongs to and instantiate it with the cmd_accessories to execute.
# Contexts:
#   Standard - Linux cmd_accessories-line qnot cmd_accessories handler.
#   Admin - qnot's cmd_accessories-prompt UI.
#
# If a user provides NO arguments from the cmd_accessories-line (only `qnot`) admin
# mode is instantiated.
def main():
    db_init()
    try:
        if len(sys.argv) == 1:
            Admin(Carg("last", [DEF_LAST]))

        elif re.findall(r"^-[a-zA-Z]+$", sys.argv[1]):
            carg: Carg = Carg(sys.argv[1].lstrip('-').lower(), sys.argv[2:])
            if carg.is_adm():
                Admin(carg)
            elif carg.is_std():
                Standard(carg)
            else:
                raise NoSuchCommand(carg.c)
        else:
            Standard(Carg('add', sys.argv[1:]))
    except KeyboardInterrupt:
        print("\nQuitting qnot.")


if __name__ == "__main__":
    main()
