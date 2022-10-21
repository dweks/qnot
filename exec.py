from util import make_dir_date, make_full_date, start_editor, file_to_string
from file import NOTES_PATH, write, write_tags
from path import Path
import parse as prs
import os


full_args = {None}
edit_args = {"last"}
view_args = {"all", "recent", "today", "last", "tag", "title"}
remove_args = {"last", "tags"}


def exec_view(args):
    pass


def exec_remove(args):
    pass


def exec_full(args):
    date = make_full_date()
    path = Path(
        NOTES_PATH,
        make_dir_date(date),
        ".TEMPNOTE",
    )

    full_path = path.get_full_path()
    start_editor(full_path)

    # Editor creates plaintext temp file; replace with json format
    if os.path.isfile(full_path):
        note = file_to_string(full_path)
        os.remove(full_path)
        note = prs.parse_note(note)
        write(note)
        if note.get_tags() is not None:
            write_tags(note.get_tags())
    else:
        print("Editor did not create file: note not created.")


def exec_edit(args):
    # deal with args if any -- get a path for start_editor
    start_editor(None)
    # if no args, open interface
    pass


