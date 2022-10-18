from path import Path
import utilities as ut
import os
import json

TAGS_FNAME = "tags.json"
LOOKUP_FNAME = "lookup.json"
SETTINGS_FNAME = "settings.json"

ASSETS_PATH = "./assets"
NOTES_PATH = "./notes"

SETTINGS_PATH = ASSETS_PATH + '/' + SETTINGS_FNAME
TAGS_PATH = ASSETS_PATH + '/' + TAGS_FNAME
LOOKUP_PATH = ASSETS_PATH + '/' + LOOKUP_FNAME


def write(note):
    full_path = note.get_path().get_full_path()
    dir_path = note.get_path().get_top_mid()

    # Create dir with today's date
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    # In off chance of duplicate fname, handle it with suffix
    if os.path.exists(full_path):
        ut.rename_duplicate(note.get_path())
        full_path = note.get_path().get_full_path()

    # Write note to json
    with open(full_path, "w") as notes_file:
        json.dump(note.dump(), notes_file, indent=4)

    if note.get_tags() is not None:
        write_tags(note.get_tags())

    # Add note with path to lookup table
    write_lookup(note)
    return 0


def write_tags(new_tags):
    path = Path(ASSETS_PATH, None, TAGS_FNAME)
    full_path = path.get_full_path()
    if not os.path.exists(full_path):
        os.mkdir(full_path)

    if os.stat(full_path).st_size != 0:
        with open(full_path, "r") as tag_file:
            tags_from_file = json.load(tag_file)

        merged_tags = list(set(tags_from_file + new_tags))
        with open(full_path, "w") as tag_file:
            json.dump(merged_tags, tag_file, indent=4)
    else:
        with open(full_path, "w") as tag_file:
            json.dump(new_tags, tag_file, indent=4)


def write_lookup(note):
    lookup = Path(ASSETS_PATH, None, LOOKUP_FNAME)
    lu_full_path = lookup.get_full_path()
    lu_dir_path = lookup.get_top()
    note_path = note.get_path()

    if not os.path.exists(lu_full_path):
        os.mkdir(lu_full_path)

    if os.stat(lu_full_path).st_size != 0:
        with open(lu_full_path, "r") as lookup:
            entries = json.load(lookup)
        entries[note_path.get_fname()] = note_path.get_full_path()
        with open(lu_full_path, "w") as lookup:
            json.dump(entries, lookup, indent=4)
    else:
        with open(lu_full_path, "w") as lookup:
            entries = {note_path.get_fname(): note_path.get_full_path()}
            json.dump(entries, lookup, indent=4)


def load_notes():
    all_notes = []
    for file in os.listdir(NOTES_PATH):
        full_path = os.path.join(NOTES_PATH + file)
        if os.path.isfile(full_path):
            with open(file, "r") as opened_file:
                all_notes.append(json.load(opened_file))
    return all_notes
