import re
from note import Note
from path import Path
from file import NOTES_PATH
import util as ut
from cmd import Command

DELIM = r"::"


def parse_raw(argv):
    if len(argv) == 1:
        # TODO make this launch the interface mode
        return None
    else:
        if re.findall(r"^-[a-zA-Z]$", argv[1]):
            return parse_command(argv)
        else:
            return parse_note(' '.join(argv[1:]))


def parse_command(argv):
    return Command(argv[1].lstrip('-').lower(), argv[2:])


def parse_note(raw_note):
    date = ut.make_full_date()
    path = Path(
        NOTES_PATH,
        ut.make_dir_date(date),
        ut.make_fname_date(date),
    )

    note, title, tags = None, None, None

    # If there is a title and the note is not ONLY a '::'
    if DELIM in raw_note and raw_note != DELIM:
        parts = raw_note.partition(DELIM)
        note = parts[2].strip()
        title = parts[0].strip() if parts[0].strip() != '' else None
    else:
        note = raw_note
    tags = extract_tags(note)
    print(tags)

    return Note(title, note, tags, path, date)


def extract_tags(to_parse):
    tags_maybe = re.findall(r"\+[a-zA-Z]+\d*", to_parse)
    if tags_maybe is None:
        return None
    tags = [tag.lstrip(' ') for tag in tags_maybe]
    tags = [tag.lstrip('+') for tag in tags]
    return tags
