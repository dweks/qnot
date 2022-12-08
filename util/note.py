from db_access import \
    tag_exists, \
    insert_note_to_notes,\
    insert_tag_to_tags,\
    create_tag_table,\
    insert_note_to_tag


def save_note(note):
    insert_note_to_notes(note)
    if note.tags is not None:
        for tag in note.tags:
            if not tag_exists(tag):
                create_tag_table(tag)
            insert_note_to_tag(tag, note.pkey)
            insert_tag_to_tags(tag)
