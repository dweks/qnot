import subprocess as sproc
import os
import sys
from utilities import file_to_string, make_dir_date, make_full_date
from file import NOTES_PATH, write, write_tags
from path import Path
import parse as prs


def edit(existing=None):
    date = make_full_date()
    path = Path(
        NOTES_PATH,
        make_dir_date(date),
        existing if existing is not None else "_TEMP",
    )
    full_path = path.get_full_path()

    # Determine default user editor (linux only so far) then
    user_editor = get_user_editor()
    # Start editor as subprocess
    run_editor = sproc.run([user_editor, full_path])
    if run_editor.returncode != 0:
        print("Something happened with the editor; note not created")
        return

    # Editor creates formatless temp file; replace with json format
    if os.path.isfile(full_path):
        note = file_to_string(full_path)
        os.remove(full_path)
        note = prs.parse_note(note)
        write(note)
        if note.get_tags() is not None:
            write_tags(note.get_tags())
    else:
        print("Editor did not create file: note not created.")


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
