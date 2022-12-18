from db_access import \
    tag_exists, \
    insert_note_to_notes,\
    insert_tag_to_tags,\
    create_tag_table,\
    insert_note_to_tag,\
    insert_tags_to_notetags,\
    create_notetags_table, \
    select_notetags


def save_note_and_tags(note):
    insert_note_to_notes(note)
    if note.tags is not None and len(note.tags) > 0:
        for tag in note.tags:
            if not tag_exists(tag):
                create_tag_table(tag)
            insert_note_to_tag(tag, note.id)
            insert_tag_to_tags(tag)
            create_notetags_table(note.id)
            insert_tags_to_notetags(note.id, tag)
    else:
        insert_note_to_tag("notag", note.id)


def add_tags_to_note(note_list):
    new_list = []
    for note in note_list:
        if note is None:
            break
        new_tags = None
        raw_tags = select_notetags(note[0])
        if raw_tags is not None:
            new_tags = [tag for tup in raw_tags for tag in tup]
        note += (new_tags,)
        new_list.append(note)
    return new_list
