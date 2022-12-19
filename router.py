from admin import Admin
from standard import Standard
from ut import re
from carg import Carg
from exceptions import NoSuchCommand

DEF_LAST = "5"


# The router determines the correct context for execution of commands from
# cmds-line arguments. If the router detects a cmds in the input (if the
# first argument begins with a `-`) it will verify which context the cmds
# belongs to and instantiate it with the cmds to execute.
# Contexts:
#   Standard - Linux cmds-line qnot cmds handler.
#   Admin - qnot's cmds-prompt UI.
#
# If a user provides NO arguments from the cmds-line (only `qnot`) admin
# mode is instantiated.
def router(argv):
    if len(argv) == 1:
        Admin(Carg("last", [DEF_LAST]))

    elif re.findall(r"^-[a-zA-Z]+$", argv[1]):
        carg = Carg(argv[1].lstrip('-').lower(), argv[2:])
        if carg.is_adm():
            Admin(carg)
        elif carg.is_std():
            Standard(carg)
        else:
            raise NoSuchCommand(carg.c)
    else:
        args = argv[1:]
        Standard(Carg('add', args))
