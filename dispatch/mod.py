from commands import cmd_edit, cmd_delete, cmd_export

mod_dispatch = {
    'e': cmd_edit,
    'edit': cmd_edit,
    'd': cmd_delete,
    'delete': cmd_delete,
    'ex': cmd_export,
    'export': cmd_export,
}
