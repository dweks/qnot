import utilities as ut
from parse import parse_note
import file as file


def handle_note(argv):
    note = parse_note(' '.join(argv))
    file.write_note(note)
    if note["tags"] is not None:
        file.write_tags(note["tags"])
