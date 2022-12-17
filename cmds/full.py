from util import prs_note, date_enc, user_editor, file_to_str, os, sp, save_note_and_tags, write_to_file, date_norm


# Entry-point for cmds called from dispatch table in Standard
#
# Gets user editor then uses editor to create a temporary file for user to edit.
# If file is saved, its contents are extracted as a string and the temp file is removed.
# The string is parsed as a note and inserted in the database

def exec_edit(note=None):
    TEMP_PATH = r"./.temp/temp_note_" + date_enc()
    func = exec_edit.__name__
    if not note:
        note_id = date_enc()
        date_c = date_norm()
        date_m = date_c
    else:
        note_id = note.id
        date_c = note.date_c
        date_m = date_norm()
        write_to_file(note, TEMP_PATH)

    editor = user_editor()
    if editor is not None:
        run_editor = sp.run([editor, TEMP_PATH])
        # Cases when opened editor is interrupted before exiting.
        if run_editor.returncode != 0:
            raise OSError(f"Editor interrupted; note not created ({func})")
    else:
        raise RuntimeError(f"No default editor found; check $EDITOR or $VISUAL; ({func})")

    if os.path.isfile(TEMP_PATH):
        new_note = prs_note(file_to_str(TEMP_PATH), note_id, date_c, date_m)
        save_note_and_tags(new_note)
        os.remove(TEMP_PATH)
    else:
        raise FileNotFoundError(f"Temporary note file not created, qnot not saved ({func})")
