import re

# TODO fix tags pattern to find tags at beginning of input
TAGS_PTRN = r" \+[a-zA-Z]+\d*"
TITLE_DELIM = r"::"


def parse_command(argv):
    cmd = argv[0]
    cargs = argv[1:]


def parse_note(note_str):
    note, title, tags = None, None, None

    if TITLE_DELIM in note_str and note_str != TITLE_DELIM:
        parts = note_str.partition(TITLE_DELIM)
        note = parts[2].strip()
        title = parts[0].strip()
    else:
        note = note_str
        title = generate_title(note)

    tags_maybe = re.findall(TAGS_PTRN, note)
    if tags_maybe:
        tags = [tag.lstrip(' ') for tag in tags_maybe]
        tags = [tag.lstrip('+') for tag in tags]

    return dict(title=title, note=note, tags=tags)


def generate_title(note):
    return ' '.join(note.split()[:3])
