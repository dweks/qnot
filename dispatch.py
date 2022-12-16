from cmds import *

admin_dispatch = {
    'a': exec_quick,
    'add': exec_quick,
    'h': exec_help,
    'help': exec_help,
    'f': exec_find,
    'find': exec_find,
    'full': exec_full,
    'ls': exec_list,
    'list': exec_list,
    'l': exec_last,
    'last': exec_last,

    'n': lambda x: "next",
    'next': lambda x: "next",
    'p': lambda x: "prev",
    'prev': lambda x: "prev",
    'q': lambda x: "quit",
    'quit': lambda x: "quit",
    'today': "_",
    'week': "_",
    'day': "_",
}

mod_dispatch = {
    'e': exec_edit,
    'edit': exec_edit,
    'r': exec_remove,
    'remove': exec_remove,
}

standard_dispatch = {
    'quick': exec_quick,
    'full': exec_full,
    'l': exec_last,
    'last': exec_last,
}

