from command import *

admin_dispatch = {
    None: lambda x: None,
    'quit': lambda x: "quit",
    'view': exec_view,
    'edit': exec_edit,
    'remove': exec_remove,
    'help': exec_help,
    'find': exec_find,
    'last': "_",
    'today': "_",
    'week': "_",
    'day': "_",
}

standard_dispatch = {
    'quick': exec_quick,
    'full': exec_full,
    'list': exec_list,
}

