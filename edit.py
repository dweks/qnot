import subprocess as sproc
import os
import sys
import utilities as ut
import file as file
from parse import parse_note


# Determine default user editor (linux only so far)
# Generate full path from passed date string
# Start editor as subprocess
# If note was created, convert contents to string then parse and write to json
# Otherwise, output "no note saved message"
def handle_edit():
    path = {
        "top": ut.NOTES_PATH,
        "day": ut.make_dir_date(),
        "file": "_TEMP",
    }
    full_path = ut.make_note_path(path)

    user_editor = get_user_editor()
    run_editor = sproc.run([user_editor, full_path])
    if run_editor.returncode != 0:
        print("Something happened with editor; note not created")
        return None
    if os.path.isfile(full_path):
        note = ut.file_to_string(full_path)
        os.remove(full_path)
        note = parse_note(note)
        file.write_note(note)
        if note["tags"] is not None:
            file.write_tags(note["tags"])
        return note
    else:
        print("Note not created.")
        return None


def get_user_editor():
    # TODO: check which os is running and use corresponding default editor
    # Find default text editor; if not found, default nano
    if sys.platform == "linux" or sys.platform == "linux2":
        editor = os.environ.get('EDITOR')
        if editor is None:
            editor = os.environ.get('VISUAL')
            if editor is None:
                print("NO DEFAULT EDITOR; Defaulting to nano")
                editor = 'nano'
        return editor
    else:
        print("Qnot will only run on linux")
        return None
