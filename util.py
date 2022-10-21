import subprocess as sproc
import sys
import datetime as dt
import os

DATE_FMT = "%m-%d-%y"
TIME_FMT = "%H%M%S"


class Fmt:
    BLD = '\033[1m'
    ITL = '\033[3m'
    UND = '\033[4m'
    END = '\033[0m'


def bld(string):
    return Fmt.BLD + string + Fmt.END


def itl(string):
    return Fmt.ITL + string + Fmt.END


def und(string):
    return Fmt.UND + string + Fmt.END


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


def start_editor(path):
    # Start editor with user's default editor
    editor = get_user_editor()
    if editor is not None:
        run_editor = sproc.run([editor, path])
        if run_editor.returncode != 0:
            print("Something happened with the editor; note not created")
    else:
        print("No editor?")


def get_user_editor():
    # TODO: check which os is running and use default editor
    # TODO: need support for non-linux
    # Find default text editor; if not found, default nano
    if sys.platform == "linux" or sys.platform == "linux2":
        editor = os.environ.get('EDITOR')
        if editor is None:
            editor = os.environ.get('VISUAL')
            if editor is None:
                print("NO DEFAULT EDITOR; Defaulting to nano")
                editor = 'nano'
        return editor
    else:
        print("Qnot will only run on linux")
        return None
