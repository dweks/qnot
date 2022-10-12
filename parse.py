import re



def parse_command(argv):
    cmd = argv[0]
    cargs = argv[1:]


def parse_note(note_str):
    if not isinstance(note_str, str):
        print("Parameter for parse() is not a string!")

    delim = r"::"
    note, title, tags = None, None, None

    if delim in note_str and note_str != delim:
        parts = note_str.partition(delim)
        note = parts[2].strip()
        title = parts[0].strip()
    else:
        note = note_str
        title = generate_title(note)

    tags = parse_tags(note)

    return dict(title=title, note=note, tags=tags)


def parse_tags(to_parse):
    # TODO fix tags pattern to find tags at beginning of input
    tags_maybe = re.findall(r" \+[a-zA-Z]+\d*", to_parse)
    if tags_maybe is None:
        return None
    tags = [tag.lstrip(' ') for tag in tags_maybe]
    tags = [tag.lstrip('+') for tag in tags]
    return tags


def generate_title(note):
    return ' '.join(note.split()[:3])
