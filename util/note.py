from db_access import \
    tag_exists, \
    insert_note_to_notes,\
    insert_tag_to_tags,\
    create_tag_table,\
    insert_note_to_tag,\
    insert_tags_to_notetags,\
    create_notetags_table


def save_note_and_tags(note):
    insert_note_to_notes(note)
    if note.tags is not None and len(note.tags) > 0:
        for tag in note.tags:
            if tag_exists(tag)[0] == 0:
                create_tag_table(tag)
            insert_note_to_tag(tag, note.id)
            insert_tag_to_tags(tag)
            create_notetags_table(note.id)
            insert_tags_to_notetags(note.id, tag)
    else:
        insert_note_to_tag("notag", note.id)
