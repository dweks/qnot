from util import os, sys


# Interacting with the user's file system

# Retrieves content of a file as a string, preserving formatting
def file_str(path):
    if os.stat(path).st_size != 0:
        with open(path, "r") as file:
            if os.path.isfile(path):
                return file.read()
    return None


# Retrieves the user's default text editor using environment variables
# If one is not found, the default is nano
# TODO: check which os is running and use default editor
# TODO: need support for non-linux
def user_editor():
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


# Writes string to a file
def write(what, where):
    pass
    # full_path = note.get_path().get_full_path()
    # dir_path = note.get_path().get_top_mid()
    #
    # # Create dir with today's date
    # if not os.path.exists(dir_path):
    #     os.mkdir(dir_path)
    #
    # # In off chance of duplicate fname, handle it with suffix
    # if os.path.exists(full_path):
    #     ut.rename_duplicate(note.get_path())
    #     full_path = note.get_path().get_full_path()
    #
    # # Write note to json
    # with open(full_path, "w") as notes_file:
    #     json.dump(note.dump(), notes_file, indent=4)
