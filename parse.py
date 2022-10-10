import datetime as dt
import re
from action import Note

DATE_FORMAT = "%Y-%m-%d_%H%M%S_%f"
TAGS_RE_PATTERN = "\+[a-zA-Z]+\d*"
TITLE_DELIMITER = "::"


def initial_parse(argv):
    if len(argv) == 1:
        return [0, str(argv[0])]
        # open interface?
        # or show help

    else:
        # check if second elm is valid command
        # if so:
        if is_command(argv[1]):
            print("all's good: ", argv[1])
            parse_command(argv[1:])
        # otherwise, must be note
        else:
            return parse_note(' '.join(argv[1:]))


def is_command(arg):
    if arg in ('h', 'v', 'a'):
        return True


def parse_command(argv):
    cmd = argv[0]
    cargs = argv[1:]


def parse_note(argv):
    date = dt.datetime.now().strftime(DATE_FORMAT)
    note, title, tags = None, None, None
    if TITLE_DELIMITER in argv and argv != "::":
        parts = argv.partition(TITLE_DELIMITER)
        note = parts[0].strip() if len(parts[1]) == 0 else parts[2].strip()
        if len(parts[1]) > 0:
            title = parts[0].strip()
        tags_maybe = re.findall(TAGS_RE_PATTERN, note)
        if tags_maybe:
            tags = [tag.lstrip('+') for tag in tags_maybe]
    else:
        note = argv
    return Note(date, title, note, tags)
