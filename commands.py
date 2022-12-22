import os
import subprocess as sp
from notetags import Note
from output import Output, Message, Listing
from db_access import select_notes_tagged_with, select_last_note, select_notetags, delete_note, select_like
from exceptions import SelectBeforeModify, NotListable, MissingArguments, MissingSearchQuery, MatchNotFound, \
    InvalidInput, FileNotExist
from ut.disp import msg, imp
from ut.date import date_norm, date_enc
from ut.note import save_note_and_tags, add_tags_to_note
from ut.file import file_to_str, write_note_to_file, user_editor
from ut.prs import parse_note, listtuple_to_list


# If an Admin object is created without parameters, this is the default
# 'dispatched' cmd_accessories.
def cmd_default(args: None = None) -> Output:
    return cmd_last(5)


# Entry-point for cmd_accessories called from dispatch in Standard
#
# Quick is the implicit cmd_accessories called when a user creates a note from
# the cmd_accessories-line. It is not callable from any other context.
def cmd_add(args: list, do_parse: bool) -> Output:
    if not args:
        raise MissingArguments("add")

    note_id: str = date_enc()
    date_c: str = date_norm()
    date_m: str = date_c
    note: Note = parse_note(' '.join(args), note_id, date_c, date_m, pure=True)

    save_note_and_tags(note)
    return Message("added", cmd_add.__name__)


# Entry-point for cmd_accessories called from dispatch table in Standard
#
# Gets user editor then uses editor to create a temporary file for user to edit.
# If file is saved, its contents are extracted as a string and the temp file is removed.
# The string is parsed as a note and inserted in the database
def cmd_edit(note: Note or None = None) -> Output:
    TEMP_PATH: str = r"./.temp/temp_note_" + date_enc()
    source: str = cmd_edit.__name__
    if not note:
        note_id = date_enc()
        date_c = date_norm()
        date_m = date_c
    else:
        note_id = note.id
        date_c = note.date_c
        date_m = date_norm()
        write_note_to_file(note, TEMP_PATH)

    editor: str or None = user_editor()
    if editor is not None:
        run_editor: sp.CompletedProcess = sp.run([editor, TEMP_PATH])
        # Cases when opened editor is interrupted before exiting.
        if run_editor.returncode != 0:
            raise OSError(f"Editor interrupted; note not created ({source})")
    else:
        raise RuntimeError(f"No default editor found; check $EDITOR or $VISUAL; ({source})")

    if os.path.isfile(TEMP_PATH):
        new_note: Note = parse_note(file_to_str(TEMP_PATH), note_id, date_c, date_m)
        save_note_and_tags(new_note)
        os.remove(TEMP_PATH)
    else:
        raise FileNotFoundError(f"Temporary note file not created, qnot not saved ({source})")

    if note is None:
        return Message("added", source)
    return Message("revised", source)


# Entry-point for cmd_accessories called from dispatch table in Admin
# Find will search the notes in the database for a provided string.
# This cmd_accessories can be called with optional parameters 'filter' and 'section'
# which alter the generation of SQL queries. If 'find' is not provided with
# a filter or section and only a search string, the default searched location
# is TODO
def cmd_get(args: list or None = None) -> Output:
    # filters: set = {'today', 'week', 'day', }

    query: list = args
    if args is None or len(args) == 0:
        query = ["notag"]
    result: list = select_notes_tagged_with(query)

    if result is None or len(result) == 0:
        raise MatchNotFound(' '.join(query))

    # TODO: change 'matching tag' to be dynamic
    return Listing(f"Matching tag: {' '.join(query)}", add_tags_to_note(result), cmd_get.__name__)


def cmd_help(args: list or None = None) -> Output:
    from dispatch.help import help_dispatch
    arg: str = "basic" if args is None else args[0]
    if arg not in help_dispatch.keys():
        raise InvalidInput("help", arg)
    else:
        print(help_dispatch[arg])
    return Message("suspend", cmd_help.__name__)


# todo: include option to parse for tags with explanation
def cmd_import(path: list or None) -> Output:
    if path is None or len(path) == 0:
        raise MissingArguments("import")
    for p in path:
        if not os.path.exists(p):
            raise FileNotExist(p)
    print(msg("Importing to qnot:"))
    for p in path:
        print(p)
    print(msg("Do you want to parse these files for qnot syntax?"))
    print(msg("This will search for a title and tags and may remove certain characters."))
    print(imp("Do not do this unless these files were created specifically for qnot!"))
    do_parse: bool = True if input(imp("Confirm parse Y/n > ")) == 'Y' else False
    for p in path:
        new_note: str = file_to_str(p)
        print(new_note)
        response: str = input(imp("Confirm add Y/n > "))
        if response == 'Y':
            cmd_add([file_to_str(p)], do_parse)
    return Message("imported", cmd_import.__name__)


def cmd_export(note: Note):
    EX_PATH = "exports/"
    if not os.path.exists(EX_PATH):
        os.mkdir(EX_PATH)
        print(msg(f"Export directory created at {EX_PATH}"))

    full_path: str = EX_PATH + "qnot_exp_" + date_enc() + ".txt"
    print(imp(f"Exporting to: {os.getcwd()}{full_path}"))
    response: str = input(imp("Confirm export Y/n > "))
    if response == 'Y':
        write_note_to_file(note, full_path)
        return Message("exported", cmd_export.__name__)
    return Message("cancel", cmd_export.__name__)


def cmd_last(args: list or None = None) -> Output:
    if args is not None:
        if not args[0].isdigit() or int(args[0]) == 0:
            raise InvalidInput("last", args[0])
        selection: int = int(args[0])
    else:
        selection = 1
    result: list or None = select_last_note(selection)
    if result is None or len(result) == 0:
        raise MatchNotFound(f"last {selection} modified")
    return Listing(f"Last {selection} modified", add_tags_to_note(result), cmd_last.__name__)


# todo make ls <num> change how many notes shown per page
def cmd_list(args: list or None = None) -> Output:
    from cmd_accessories.list import dispatch
    if args is None:
        return Message("show", cmd_list.__name__)
    if args[0] not in dispatch.keys():
        raise NotListable(args[0])
    dispatch[args[0]]()
    return Message("suspend", cmd_list.__name__)


# Entry-point for cmd_accessories called from dispatch table in Admin
def cmd_delete(note: Note or None) -> Output:
    if note is None:
        raise SelectBeforeModify("delete.")
    tags: list = []
    print(imp('\nPERMANENTLY DELETING NOTE:'))
    note.print_long()
    response: str = input(imp("Confirm delete Y/n > "))
    if response == 'Y':
        if note.tags is not None and not note.tags.empty():
            tags = select_notetags(note.id)
            if tags:
                tags = listtuple_to_list(tags)
        delete_note(note.id, tags)
        return Message("deleted", cmd_delete.__name__)
    return Message("cancel", cmd_delete.__name__)


def cmd_search(query: list or None) -> Output:
    if query is None:
        raise MissingSearchQuery("search")
    result: list = select_like(query)
    if result is None or len(result) == 0:
        raise MatchNotFound(f"{' '.join(query)}")
    return Listing(f"Searching for ` {' '.join(query)} `", add_tags_to_note(result), cmd_search.__name__)
