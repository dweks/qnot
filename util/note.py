from db_access import \
    tag_exists, \
    insert_note_to_notes,\
    insert_tag_to_tags,\
    create_tag_table,\
    insert_note_to_tag


def save_note(note):
    insert_note_to_notes(note)
    if note.tags is not None and len(note.tags) > 0:
        for tag in note.tags:
            t = tag_exists(tag)
            if t is None or len(t) == 0:
                create_tag_table(tag)
            insert_note_to_tag(tag, note.pkey)
            insert_tag_to_tags(tag)
    else:
        insert_note_to_tag("notag", note.pkey)
