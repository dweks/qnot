import os
import json

TAGS_PATH = "./temp_save/"
TAGS_FILENAME = "tags.json"
TAGS_FULL_PATH = TAGS_PATH + TAGS_FILENAME
NOTES_PATH = "./temp_save/notes/"


def write(note):
    if note.data["tags"] is not None:
        write_tags(note.data["tags"])
    if note.data["note"] is not None:
        write_note(note)


def write_tags(new_tags):
    if os.stat(TAGS_FULL_PATH).st_size != 0:
        with open(TAGS_FULL_PATH, "r") as tag_file:
            file_tags = json.load(tag_file)
        merged_tags = list(set(file_tags + new_tags))
        with open(TAGS_FULL_PATH, "w") as tag_file:
            json.dump(merged_tags, tag_file)
    else:
        with open(TAGS_FULL_PATH, "w") as tag_file:
            json.dump(new_tags, tag_file)


def write_note(parsed):
    file_name = NOTES_PATH + parsed.data["date"]
    with open(file_name + ".json", "w") as notes_file:
        json.dump(parsed.data, notes_file)


def load_notes():
    all_notes = []
    for file in os.listdir(NOTES_PATH):
        full_path = os.path.join(NOTES_PATH + file)
        if os.path.isfile(full_path):
            with open(file, "r") as opened_file:
                all_notes.append(json.load(opened_file))
    return all_notes
