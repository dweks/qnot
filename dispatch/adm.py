import commands as cmd
admin_dispatch = {
    'a': cmd.exec_add,
    'add': cmd.exec_add,
    'h': cmd.exec_help,
    'help': cmd.exec_help,
    'g': cmd.exec_get,
    'get': cmd.exec_get,
    'f': cmd.exec_edit,
    'full': cmd.exec_edit,
    'ls': cmd.exec_list,
    'list': cmd.exec_list,
    'l': cmd.exec_last,
    'last': cmd.exec_last,
    's': cmd.exec_search,
    'search': cmd.exec_search,

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

