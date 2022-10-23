from path import Path
import util as ut
import os
import json

TAGS_FNAME = r"tags.json"
LOOKUP_FNAME = r"lookup.json"
SETTINGS_FNAME = r"settings.json"
DB_FNAME = r"qnot.db"

ASSETS_PATH = r"./assets"
DB_PATH = r"./notes"

DB_FULL = DB_PATH + '/' + DB_FNAME
SETTINGS_PATH = ASSETS_PATH + '/' + SETTINGS_FNAME
TAGS_PATH = ASSETS_PATH + '/' + TAGS_FNAME


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

