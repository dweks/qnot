from admin import Admin
from standard import Standard
from util import re
from dispatch import admin_dispatch, standard_dispatch


# The router determines the correct context for execution of commands from
# command-line arguments. If the router detects a command in the input (if the
# first argument begins with a `-`) it will verify which context the command
# belongs to and instantiate it with the command to execute.
# Contexts:
#   Standard - Linux command-line qnot command handler.
#   Admin - qnot's command-prompt UI.
#
# If a user provides NO arguments from the command-line (only `qnot`) admin
# mode is instantiated.

def router(argv):
    if len(argv) == 1:
        Admin()

    elif re.findall(r"^-[a-zA-Z]+$", argv[1]):
        cmd = argv[1].lstrip('-').lower()
        args = argv[2:]
        if cmd in admin_dispatch.keys():
            Admin(cmd, args)
        elif cmd in standard_dispatch.keys():
            Standard(cmd, args)
        else:
            raise ValueError(f"Invalid command: '{cmd}'")
    else:
        args = argv[1:]
        Standard('quick', args)
