from util import prs_note, save_note_and_tags, date_enc, date_norm, debug


# Entry-point for cmds called from dispatch in Standard
#
# Quick is the implicit cmds called when a user creates a note from
# the cmds-line. It is not callable from any other context.
def exec_quick(args):
    note_id = date_enc()
    date_c = date_norm()
    date_m = date_c
    note = prs_note(' '.join(args), note_id, date_c, date_m)
    save_note_and_tags(note)
    return "added"
