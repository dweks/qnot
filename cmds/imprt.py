from .add import exec_add
import ut
from exceptions import MissingArguments


def exec_import(path):
    if not path or len(path) == 0:
        raise MissingArguments("import")
    for p in path:
        new_note = ut.file_to_str(p)
        print(new_note)
        response = input(ut.imp("Confirm add Y/n > "))
        if response == 'Y':
            exec_add([ut.file_to_str(p)])
