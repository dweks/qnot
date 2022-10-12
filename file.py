import utilities as ut
import os
import json


def write_generic(file, path):
    pass
    # TODO add some success communication of written correctly


def write_note(parsed):
    path = {
        "top": ut.NOTES_PATH,
        "day": ut.make_dir_date(),
        "file": ut.replace_spaces(parsed["title"], '_'),
    }

    # full_path = path["top"] + path["day"] + path["file"]
    full_path = ut.make_note_path(path)
    dir_path = path["top"] + path["day"]

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    if os.path.exists(full_path):
        path["file"] = ut.rename_duplicate(path)
        full_path = ut.make_note_path(path)

    with open(full_path, "w") as notes_file:
        json.dump(parsed, notes_file, indent=4)

    if not os.path.exists(full_path):
        return -1
    return 0


def write_tags(new_tags):
    # TODO add some success communication of written correctly
    if not os.path.exists(ut.TAGS_PATH):
        return -1
    if os.stat(ut.TAGS_PATH).st_size != 0:
        with open(ut.TAGS_PATH, "r") as tag_file:
            tags_from_file = json.load(tag_file)
        merged_tags = list(set(tags_from_file + new_tags))
        with open(ut.TAGS_PATH, "w") as tag_file:
            json.dump(merged_tags, tag_file, indent=4)
    else:
        with open(ut.TAGS_PATH, "w") as tag_file:
            json.dump(new_tags, tag_file, indent=4)


def load_notes():
    all_notes = []
    for file in os.listdir(ut.NOTES_PATH):
        full_path = os.path.join(ut.NOTES_PATH + file)
        if os.path.isfile(full_path):
            with open(file, "r") as opened_file:
                all_notes.append(json.load(opened_file))
    return all_notes
