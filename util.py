import datetime as dt
import os

DATE_FMT = "%m-%d-%y"
TIME_FMT = "%H%M%S"


def make_full_date():
    return dt.datetime.now()


def make_dir_date(date):
    return date.strftime(DATE_FMT)


def make_fname_date(date):
    return date.strftime(TIME_FMT)


def rename_duplicate(path):
    original = path.get_fname()
    updated = original
    count = 1
    while os.path.exists(path.get_full_path()):
        updated = original
        updated += f"_{count}"
        count += 1
    path.set_fname(updated)


def replace_spaces(string, char):
    return char.join(string.split())


def file_to_string(path):
    if os.stat(path).st_size != 0:
        with open(path, "r") as file:
            if os.path.isfile(path):
                return file.read()
    return None
