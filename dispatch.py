from cmds import *

admin_dispatch = {
    'a': exec_add,
    'add': exec_add,
    'h': exec_help,
    'help': exec_help,
    'g': exec_get,
    'get': exec_get,
    'f': exec_edit,
    'full': exec_edit,
    'ls': exec_list,
    'list': exec_list,
    'l': exec_last,
    'last': exec_last,
    's': exec_search,
    'search': exec_search,

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
    'd': exec_delete,
    'delete': exec_delete,
    'ex': exec_export,
    'export': exec_export,
}

std_dispatch = {
    'add': exec_add,
    'f': exec_edit,
    'full': exec_edit,
    'l': exec_last,
    'last': exec_last,
    'i': exec_import,
    'import': exec_import,
}
