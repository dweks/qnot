from commands import cmd_edit, cmd_delete, cmd_export, cmd_merge
from output import Message

mod_dispatch = {
    'e': cmd_edit,
    'edit': cmd_edit,
    'del': cmd_delete,
    'delete': cmd_delete,
    'ex': cmd_export,
    'export': cmd_export,
    'm': cmd_merge,
    'merge': cmd_merge,
    'x': lambda x: Message("exit"),
    'exit': lambda x: Message("exit"),
    'q': lambda x: Message("quit"),
    'quit': lambda x: Message("quit"),
    'n': lambda x: Message("next"),
    'next': lambda x: Message("next"),
    'p': lambda x: Message("prev"),
    'prev': lambda x: Message("prev"),
}
