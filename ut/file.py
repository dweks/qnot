import os
from sys import platform


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


# Writes string to a file
def note_to_file(note, path) -> None:
    title_maybe: str = ''
    if note.title is not None and note.title != "None":
        title_maybe = note.title + " :: "
    with open(path, "w") as notes_file:
        notes_file.write(title_maybe + note.body)

