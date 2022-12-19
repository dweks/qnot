import ut
from exceptions import MissingArguments


# Entry-point for cmds called from dispatch in Standard
#
# Quick is the implicit cmds called when a user creates a note from
# the cmds-line. It is not callable from any other context.
def exec_add(args):
    if not args:
        raise MissingArguments("add")
    note_id = ut.date_enc()
    date_c = ut.date_norm()
    date_m = date_c
    note = ut.prs_note(' '.join(args), note_id, date_c, date_m)
    ut.save_note_and_tags(note)
    return "added"
