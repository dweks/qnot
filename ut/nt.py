import db_access as db
from note import Note


def save_note_and_tags(note: Note):
    db.insert_note_to_notes(note)
    if note.tags is not None and len(note.tags) > 0:
        for tag in note.tags:
            if not db.tag_exists(tag):
                db.create_tag_table(tag)
            db.insert_note_to_tag(tag, note.id)
            db.insert_tag_to_tags(tag)
            db.create_notetags_table(note.id)
            db.insert_tags_to_notetags(note.id, tag)
    else:
        db.insert_note_to_tag("notag", note.id)


def add_tags_to_note(notes: list) -> list:
    tagged_notes: list = []
    for note in notes:
        if note is None:
            break
        new_tags: list = []
        raw_tags: tuple[list] = db.select_notetags(note[0])
        if raw_tags is not None:
            new_tags = [tag for tup in raw_tags for tag in tup]
        note += (new_tags,)
        tagged_notes.append(note)
    return tagged_notes
