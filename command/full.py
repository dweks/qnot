from util import prs_note, date_enc, user_editor, file_str, os, sp, save_note


# Entry-point for command called from dispatch table in Standard
#
# Gets user editor then uses editor to create a temporary file for user to edit.
# If file is saved, its contents are extracted as a string and the temp file is removed.
# The string is parsed as a note and inserted in the database

def exec_full(args=None):
    # TODO figure out what to do with this function's args
    TEMP_PATH = r"./.temp/temp_note_" + date_enc()
    func = exec_full.__name__

    editor = user_editor()
    if editor is not None:
        run_editor = sp.run([editor, TEMP_PATH])
        # Cases when opened editor is interrupted before exiting.
        if run_editor.returncode != 0:
            raise OSError(f"Editor interrupted; note not created ({func})")

    else:
        raise RuntimeError(f"No default editor found; check $EDITOR or $VISUAL? ({func})")

    # Remove temp file, parse note, insert to database
    if os.path.isfile(TEMP_PATH):
        note = file_str(TEMP_PATH)
        os.remove(TEMP_PATH)
        note = prs_note(note)

        save_note(note)
    else:
        raise FileNotFoundError(f"Temporary note file not created, qnot not saved ({func})")
