from util import re, date_enc, date_norm
TITLE_DELIM = '::'


# Parses a raw note string to title and body partitions.
# For title:
#   Searches for first occurence of title delimiter and
#   considers anything before it as the title.
# For body:
#   Anything other than a found title is considered the
#   body of the note.
def prs_note(raw_note):
    title, body, tags = None, None, None
    pkey = date_enc()
    date = date_norm()

    if TITLE_DELIM in raw_note:
        parts = raw_note.partition(TITLE_DELIM)
        title = parts[0].strip() if parts[0].strip() != '' else None
        body = parts[2].strip()
    else:
        body = raw_note
    tags = parse_tags(body)
    if title:
        tags += parse_tags(title)

    return dict(pkey=pkey, title=title, body=body, tags=tags, date=date)


# Finds all occurences of substrings with the 'tag' syntax
# anywhere in the given string and returns a list of them
# without the delimiter.
def parse_tags(to_parse):
    tags_maybe = re.findall(r"\+[a-zA-Z]+\w*", to_parse)
    if tags_maybe is None:
        return None
    tags = [tag.lstrip(' ') for tag in tags_maybe]
    tags = [tag.lstrip('+') for tag in tags]
    return tags
