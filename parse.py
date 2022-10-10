import datetime as dt
import re
from note import Note

DATE_FORMAT = "%Y-%m-%d_%H-%m_%f"
TAGS_RE_PATTERN = "\+[a-zA-Z]+\d*"


def initial_parse(argv):
    if len(argv) == 1:
        return [0, str(argv)]
        # open interface?
        # or show help

    else:
        # check if second elm is valid command
        # if so:
        if is_command(argv[1]):
            parse_command(' '.join(argv[1:]))
        # otherwise, must be note
        else:
            return parse_note(' '.join(argv[1:]))


def is_command(arg):
    return False


def parse_note(argv):
    date = dt.datetime.now().strftime(DATE_FORMAT)
    partition = argv.partition("::")

    if len(partition[1]) == 0:
        note = partition[0]
        title = None
    else:
        title = partition[0]
        note = partition[2]

        tags_maybe = re.findall(TAGS_RE_PATTERN, note)
        tags = tags_maybe if len(tags_maybe) > 0 else None

        if title:
            title = title.strip()
        if note:
            note = note.strip()
        if tags:
            tags = [tag.lstrip('+') for tag in tags]

        return Note(date, title, note, tags)


def parse_command(interim):
    pass