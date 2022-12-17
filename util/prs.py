from util import re, date_enc, date_norm
from note import Note
TITLE_DELIM = '::'
TAG_PATTERN = r"\+[a-zA-Z]+\w*\s*"

# Parses a raw note string to title and body partitions.
# For title:
#   Searches for first occurence of title delimiter and
#   considers anything before it as the title.
# For body:
#   Anything other than a found title is considered the
#   body of the note.
def prs_note(raw_note):
    title, body, tags = None, None, None

    if TITLE_DELIM in raw_note:
        parts = raw_note.partition(TITLE_DELIM)
        title = parts[0].strip() if parts[0].strip() != '' else None
        body = parts[2].strip()
    else:
        body = remove_tag_notation(raw_note)
    tags = parse_tags(body)
    if title:
        tags += parse_tags(title)

    return Note(date_enc(), title, body, tags, date_norm())


# Finds all occurences of substrings with the 'tag' syntax
# anywhere in the given string and returns a list of them
# without the delimiter.
def parse_tags(to_parse):
    tags_maybe = re.findall(TAG_PATTERN, to_parse)
    if tags_maybe is None:
        return None
    tags = [tag.lstrip(' ') for tag in tags_maybe]
    tags = [tag.lstrip('+') for tag in tags]
    return tags


def remove_tag_notation(to_parse):
    split = to_parse.split(' ')
    split = [part.lstrip('+') for part in split]
    return ' '.join(split)
