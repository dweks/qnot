import datetime as dt
import os

ASSETS_PATH = "./assets/"
TAGS_FNAME = "tags.json"
SETTINGS_PATH = "./settings.json"
TAGS_PATH = ASSETS_PATH + TAGS_FNAME
NOTES_PATH = "./notes/"

DATE_FMT = "%m-%d-%y"


def make_dir_date():
    return dt.datetime.now().strftime(DATE_FMT) + '/'


def rename_duplicate(path):
    original = path["file"]
    count = 1
    while os.path.exists(make_note_path(path)):
        path["file"] = original
        path["file"] += f"_{count}"
        count += 1
    return path["file"]


def replace_spaces(string, char):
    return char.join(string.split())


def make_note_path(path):
    return ''.join(path.values()) + '.json'


def file_to_string(path):
    if os.stat(path).st_size != 0:
        with open(path, "r") as file:
            if os.path.isfile(path):
                return file.read()
    return None
