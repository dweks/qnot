from util import prs_note, save_note


# Entry-point for cmds called from dispatch in Standard
#
# Quick is the implicit cmds called when a user creates a note from
# the cmds-line. It is not callable from any other context.
def exec_quick(args):
    note = prs_note(' '.join(args))
    save_note(note)
    return "added"
