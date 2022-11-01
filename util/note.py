from db.insert import ins_note, ins_tag_row


def save_note(note):
    ins_note(note)
    if note["tags"] is not None:
        for tag in note["tags"]:
            ins_tag_row(tag)
