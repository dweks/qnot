from db_access import remove_note
from util import imp
from exceptions import SelectBeforeModify


# Entry-point for cmds called from dispatch table in Admin
def exec_remove(note) -> str:
    if note is None:
        raise SelectBeforeModify("remove.")
    print(imp('PERMANENTLY DELETING NOTE:'))
    note.print_oneline()
    response = input("Confirm Y/n > ")
    if response == 'Y':
        remove_note(note)
        return "deleted"
    return "cancel"
