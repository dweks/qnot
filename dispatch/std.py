from commands import exec_add, exec_edit, exec_last, exec_import
std_dispatch = {
    'add': exec_add,
    'f': exec_edit,
    'full': exec_edit,
    'l': exec_last,
    'last': exec_last,
    'i': exec_import,
    'import': exec_import,
}

