from commands import exec_edit, exec_delete, exec_export

mod_dispatch = {
    'e': exec_edit,
    'edit': exec_edit,
    'd': exec_delete,
    'delete': exec_delete,
    'ex': exec_export,
    'export': exec_export,
}
