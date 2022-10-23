from util import make_dir_date, make_full_date, start_editor, file_to_str
from file import DB_PATH, write, write_tags
from path import Path
import parse as prs
import os


def exec_full(args=None):
    date = make_full_date()
    path = Path(
        DB_PATH,
        make_dir_date(date),
        ".TEMPNOTE",
    )

    full_path = path.get_full_path()
    start_editor(full_path)

    # Editor creates plaintext temp file; replace with json format
    if os.path.isfile(full_path):
        note = file_to_str(full_path)
        os.remove(full_path)
        note = prs.parse_note(note)
        write(note)
        if note.get_tags() is not None:
            write_tags(note.get_tags())
    else:
        print("Editor did not create file: note not created.")
