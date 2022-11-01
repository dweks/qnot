from util import prs_note, save_note


# Entry-point for command called from dispatch in Standard
#
# Quick is the implicit command called when a user creates a note from
# the command-line. It is not callable from any other context.
def exec_quick(args):
    note = prs_note(' '.join(args))
    save_note(note)
