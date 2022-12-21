import re
from note import Note

TITLE_DELIM: str = '::'
TAG_PATTERN: str = r"\s*\+[a-zA-Z]+\w*\s*"


# Parses a raw note string to title and body partitions.
# For title:
#   Searches for first occurence of title delimiter and
#   considers anything before it as the title.
# For body:
#   Anything other than a found title is considered the
#   body of the note.
def parse_note(note: str, note_id: str, date_c: str, date_m: str) -> Note:
    tags = parse_tags(note)
    note = remove_tag_notation(note)

    if TITLE_DELIM in note:
        parts: tuple[str, str, str] = note.partition(TITLE_DELIM)
        title: str or None = parts[0].strip() if parts[0].strip() != '' else None
        body: str = parts[2].strip()
    else:
        title = None
        body = note

    return Note(note_id, title, body, date_c, date_m, tags)


# Finds all occurences of substrings with the 'tag' syntax
# anywhere in the given string and returns a list of them
# without the delimiter.
def parse_tags(tags: str) -> list:
    tags_maybe: list or None = re.findall(TAG_PATTERN, tags)
    print(tags_maybe)
    if len(tags_maybe) == 0:
        return tags_maybe
    p_tags = [tag.strip(' ') for tag in tags_maybe]
    p_tags = [tag.strip('\n') for tag in p_tags]
    p_tags = [tag.lstrip('+') for tag in p_tags]
    return p_tags


def remove_tag_notation(to_parse: str) -> str:
    split: list = to_parse.split(' ')
    split = [part.lstrip('+') for part in split]
    return ' '.join(split)


