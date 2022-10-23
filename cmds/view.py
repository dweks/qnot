import json
from display import code
import os
from util import file_to_str
from file import DB_PATH


# TODO put together some dummy notes to test with

def exec_view(args):
    view_filters = {
        "all": filt_all,
        "recent": filt_recent,
        "today": filt_today,
        "last": filt_last,
        "tag": filt_tag,
        "title": filt_title,
        "help": filt_help,
        "quit": lambda null: True,
        None: lambda null: False,
    }
    if not args:
        print("NO VIEW FILTERS PROVIDED; INTERFACE MODE")

        done = False
        while not done:
            subcmd = input("\n> ").split()
            filt = subcmd[0] if len(subcmd) >= 1 else None
            by = subcmd[1:] if len(subcmd) >= 2 else None

            found_notes = view_filters[filt](by)
            if not found_notes:
                print("Invalid entry")
            else:
                lister(found_notes)


def lister(found_notes):
    # TODO have a maximum display with a "view more?" option
    len_cap = 40
    count = 1
    for entry in found_notes:
        title = entry["title"]
        note = entry["note"]
        tags = entry["tags"]

        print(f"({count}) ", note if len(note) <= len_cap else entry[:40])
        count += 1


def filt_help(args=None):
    print("Choose a 'recent' number, or choose from: ")
    return False


def filt_title(args):
    if not args:
        print("Enter a title to search for.")
        return None

    hold = []
    for root, dirs, files in os.walk("./notes"):
        for name in files:
            json_str = file_to_str(os.path.join(root, name))
            note_dict = json.loads(json_str)
            if note_dict["title"] == ' '.join(args):
                hold.append(note_dict)
    return hold


def filt_tag(note):
    if not note["tags"]:
        return False
    return True


# This one needs a date and time
# maybe use lookup?
def filt_last(note):
    pass


def filt_recent(note):
    pass


def filt_today(note):
    pass


def filt_all(note):
    hold = []
    for root, dirs, files in os.walk("./notes"):
        for name in files:
            json_str = file_to_str(os.path.join(root, name))
            note_dict = json.loads(json_str)
            hold.append(note_dict)

    print(hold)