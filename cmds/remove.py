from db_access import delete_note, select_notetags
from ut import imp, debug
from exceptions import SelectBeforeModify


# Entry-point for cmds called from dispatch table in Admin
def exec_remove(note) -> str:
    if note is None:
        raise SelectBeforeModify("remove.")
    tags = []
    print(imp('\nPERMANENTLY DELETING NOTE:'))
    note.print_full()
    response = input("Confirm Y/n > ")
    if response == 'Y':
        if note.tags and len(note.tags) > 0:
            tags = select_notetags(note.id)
            if tags:
                tags = [tag for tup in tags for tag in tup]
        delete_note(note.id, tags)
        return "deleted"
    return "cancel"
