import re
from notetags import Note, Tags
# from ut.debug import ldebug, debug

TITLE_DELIM: str = '::'
PAT_BARE_TAG: str = r'[a-zA-Z0-9]+'
PAT_REG_TAG: str = r'\b_' + PAT_BARE_TAG + r'\b'
PAT_GROUP_TAG: str = r'\b__[\s*' + PAT_BARE_TAG + r'\s*__\b'


# Parses a raw note string to title and body partitions.
# For title:
#   Searches for first occurence of title delimiter and
#   considers anything before it as the title.
# For body:
#   Anything other than a found title is considered the
#   body of the note.
def parse_note(raw_note: str, note_id: str, date_c: str, date_m: str, pure=False) -> Note:
    if not pure:
        tags = Tags(parse_tags(raw_note))
        raw_note = remove_tag_notation(raw_note)

        if TITLE_DELIM in raw_note:
            parts: tuple = raw_note.partition(TITLE_DELIM)
            title: str or None = parts[0].strip() if parts[0].strip() != '' else None
            body: str = parts[2].strip()
        else:
            title = None
            body = raw_note
        return Note(note_id, title, body, date_c, date_m, tags)
    else:
        return Note(note_id, None, raw_note, date_c, date_m, Tags())




# Finds all occurences of substrings with the 'tag' syntax
# anywhere in the given string and returns a list of them
# without the delimiter.
def parse_tags(raw_note: str) -> list:
    # ldebug("raw", raw_note)
    p_tags: list or None = re.findall(PAT_REG_TAG, raw_note)
    # ldebug("reg", p_tags)
    p_tags += re.findall(PAT_GROUP_TAG, raw_note)
    # ldebug("after group", p_tags)
    p_tags = re.findall(PAT_BARE_TAG, ' '.join(p_tags))
    if len(p_tags) == 0:
        # debug("no tags found")
        return p_tags
    p_tags = [tag.strip(' ') for tag in p_tags]
    p_tags = [tag.strip('\n') for tag in p_tags]
    p_tags = [tag.lstrip('_') for tag in p_tags]
    # ldebug("FINAL", p_tags)
    return p_tags


def remove_tag_notation(raw_note: str) -> str:
    # ldebug("raw before", raw_note)
    raw_note = re.sub(PAT_GROUP_TAG, '', raw_note)
    # ldebug("raw after", raw_note)
    split: list = raw_note.split(' ')
    split = [part.lstrip('_') for part in split]
    return ' '.join(split)


def listtuple_to_list(listtuple: list) -> list:
    return [item for tup in listtuple for item in tup]
