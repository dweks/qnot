import re
from notetags import Note, Tags
from exceptions import InvalidSelection
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
            body: str = parts[2]
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
    p_tags: list or None = re.findall(PAT_REG_TAG, raw_note)
    p_tags += re.findall(PAT_GROUP_TAG, raw_note)
    p_tags = re.findall(PAT_BARE_TAG, ' '.join(p_tags))
    if len(p_tags) == 0:
        return p_tags
    p_tags = [tag.strip(' ') for tag in p_tags]
    p_tags = [tag.strip('\n') for tag in p_tags]
    p_tags = [tag.lstrip('_') for tag in p_tags]
    return p_tags


def remove_tag_notation(raw_note: str) -> str:
    raw_note = re.sub(PAT_GROUP_TAG, '', raw_note)
    raw_note = ' '.join([part.lstrip('_') for part in raw_note.split(' ')])
    return '\n'.join([part.strip('_') for part in raw_note.split('\n')])


def detuple(listtuple: list) -> list:
    return [item for tup in listtuple for item in tup]


def parse_selection(sel: list) -> tuple:
    maybe_slice: list = [s for s in sel if '-' in s]
    slices: list = []
    if len(maybe_slice) > 0:
        for item in maybe_slice:
            if item.count('-') == 1:
                parts: tuple = item.partition('-')
                if parts[0].isdigit() and parts[2].isdigit():
                    if int(parts[0]) < int(parts[2]):
                        slices.append(slice(int(parts[0]) - 1, int(parts[2])))
                    else:
                        raise InvalidSelection(item)
                else:
                    raise InvalidSelection(item)
            else:
                raise InvalidSelection(item)

    maybe_singles: list = [s for s in sel if '-' not in s]
    singles: list = []
    if len(maybe_singles) > 0:
        for s in maybe_singles:
            if not s.isdigit():
                raise InvalidSelection(s)
            singles.append(int(s) - 1)
    return slices, singles
