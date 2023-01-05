import db_access as db
from notetags import Note, Tags, NOTAG
from ut.prs import detuple
from ut.disp import f
# from ut.debug import debug


def save_note_and_tags(note: Note):
    db.insert_note_to_notes(note)
    if not note.tags.empty():
        for tag in note.tags.tags:
            if not db.tag_exists(tag):
                db.create_tag_table(tag)
            db.insert_note_to_tag(note.id, tag)
            db.insert_tag_to_tags(tag)
            db.create_notetags_table(note.id)
            db.insert_tags_to_notetags(note.id, tag)
    else:
        db.insert_note_to_tag(note.id, NOTAG)


def add_tags_to_note(notes: list) -> list:
    tagged_notes: list = []
    for note in notes:
        list(note)
        if note is None:
            break
        new_tags: Tags = Tags([])
        raw_tags: list = db.select_notetags(note[0])
        if raw_tags is not None:
            new_tags += detuple(raw_tags)
        note += (new_tags,)
        tagged_notes.append(note)
    return tagged_notes


def deparse_title(title: str) -> str:
    return title + " :: " if title is not None and title != "None" else ''


def deparse_tags(tags: set) -> str:
    return '\n__ ' + ' '.join(tags) + ' __'


def confirm(text: str) -> bool:
    return True if input(f(f"Confirm {text} Y/n > ", 'lc')) == 'Y' else False
