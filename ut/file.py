import os
from sys import platform
from notetags import Note
from ut.note import deparse_title, deparse_tags


# Retrieves content of a file as a string, preserving formatting
def file_to_str(path) -> str or None:
    if os.stat(path).st_size != 0:
        with open(path, "r") as file:
            if os.path.isfile(path):
                return file.read()
    return None


# Retrieves the user's default text editor using environment variables
# If one is not found, the default is nano
def user_editor() -> os.environ or None:
    if platform == "linux" or platform == "linux2":
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


def note_to_file(note: Note, path: str, mode='w') -> None:
    with open(path, mode) as notes_file:
        notes_file.write(deparse_title(note.title) + note.body + deparse_tags(note.tags.tags))
