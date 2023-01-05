import os
import subprocess as sp
from notetags import Note, NOTAG, Tags
from output import Output, Message, Listing
from db_access import select_notes_tagged_with, select_last_note, select_notetags, delete_note, select_like
from exceptions import SelectBeforeModify, NotListable, MissingArguments, MissingSearchQuery, MatchNotFound, \
    InvalidInput, FileNotExist, EmptyDirectory
from ut.disp import f, imp, suc, warn, heading
from ut.date import date_norm, date_enc, encode_norm
from ut.note import save_note_and_tags, add_tags_to_note, confirm, deparse_title
from ut.file import file_to_str, note_to_file, user_editor
from ut.prs import parse_note, detuple


# Entry-point for cmd_accessories called from dispatch in Standard
# Quick is the implicit cmd_accessories called when a user creates a note from
# the cmd_accessories-line. It is not callable from any other context.
def cmd_add(args: list, join: bool = True, pure: bool = False) -> Output:
    if len(args) == 0:
        raise MissingArguments("add")

    note_id: str = date_enc()
    date_c: str = date_norm()
    date_m: str = date_c
    note: Note = parse_note(' '.join(args) if join else args, note_id, date_c, date_m, pure=pure)

    save_note_and_tags(note)
    return Message("added", suc("Note added."))


# Entry-point for cmd_accessories called from dispatch table in Standard
#
# Gets user editor then uses editor to create a temporary file for user to edit.
# If file is saved, its contents are extracted as a string and the temp file is removed.
# The string is parsed as a note and inserted in the database
def cmd_edit(maybe_note: list = None) -> Output:
    TEMP_PATH: str = r"./.temp/qnot_temp_" + date_enc()
    if len(maybe_note) > 0:
        note_to_file(maybe_note[0], TEMP_PATH)
    source: str = cmd_edit.__name__
    editor: str or None = user_editor()
    if editor is not None:
        run_editor: sp.CompletedProcess = sp.run([editor, TEMP_PATH])
        # Cases when opened editor is interrupted before exiting.
        if run_editor.returncode != 0:
            raise OSError(f"Editor interrupted; note not created ({source})")
    else:
        raise RuntimeError(f"No default editor found; check $EDITOR or $VISUAL; ({source})")

    if not os.path.isfile(TEMP_PATH):
        raise FileNotFoundError(f"Temporary note file not created, qnot not saved ({source})")

    if len(maybe_note) == 0:
        d_norm: str = date_norm()
        save_note_and_tags(parse_note(file_to_str(TEMP_PATH), date_enc(), d_norm, d_norm))
        os.remove(TEMP_PATH)
        return Message("added", suc("Note added."))
    else:
        # todo include possibility that file was not changed
        save_note_and_tags(parse_note(file_to_str(TEMP_PATH), maybe_note[0].id, maybe_note[0].date_c, date_norm()))
        os.remove(TEMP_PATH)
        return Message("revised", suc("Revisions saved."))


# Entry-point for cmd_accessories called from dispatch table in Admin
# Find will search the notes in the database for a provided string.
# This cmd_accessories can be called with optional parameters 'filter' and 'section'
# which alter the generation of SQL queries. If 'find' is not provided with
# a filter or section and only a search string, the default searched location
# is TODO
def cmd_get(args: list) -> Output:
    # filters: set = {'today', 'week', 'day', }

    query: list = args
    if len(args) == 0:
        query = [NOTAG]
    result: list = select_notes_tagged_with(query)

    if result is None or len(result) == 0:
        raise MatchNotFound(' '.join(query))

    # TODO: change 'matching tag' to be dynamic
    return Listing(f"Matching tag: {' '.join(query)}", add_tags_to_note(result))


def cmd_help(args: list) -> Output:
    from dispatch.help import help_dispatch
    arg: str = "basic" if len(args) == 0 else args[0]
    if arg not in help_dispatch.keys():
        raise InvalidInput("help", arg)
    else:
        print(help_dispatch[arg])
    return Message("hide")


# todo: include option to parse for tags with explanation
def cmd_import(paths: list) -> Output:
    if len(paths) == 0:
        raise MissingArguments("import")
    if len(paths) == 1 and os.path.isdir(paths[0]):
        paths = os.listdir(paths[0])
        if len(paths) == 0:
            raise EmptyDirectory(paths[0])
    print(paths)
    for p in paths:
        if not os.path.exists(p):
            raise FileNotExist(p)
    print(heading("Importing files to qnot:"))
    for p in paths:
        print(p)
    print("Do you want to parse these files for qnot syntax?")
    print("  This will search for a title and tags and may remove certain characters.")
    print(f("  Do not do this unless these files were created specifically for qnot!", s='i'))
    do_parse: bool = confirm("parse")
    if confirm("add"):
        for p in paths:
            cmd_add([file_to_str(p)], pure=do_parse)
        return Message("imported", suc("Notes imported."))
    return Message("cancel", warn("Notes not imported."))


def cmd_export(notes: list):
    # todo accomodate to lists of notes
    EX_PATH = "exports/"
    export_suc: int = 0
    if not os.path.exists(EX_PATH):
        os.mkdir(EX_PATH)
        print(heading(f"Export directory created at {EX_PATH}"))

    print(imp(f'\nExporting {len(notes)} notes to {os.getcwd()}/{EX_PATH}'))
    print(warn("Notes will also remain in qnot."))
    if confirm("export"):
        for note in notes:
            full_path: str = EX_PATH + "qnot_exp_" + encode_norm(note.get_datem_obj()) + ".txt"
            if os.path.exists(full_path):
                print(imp('File already exists:'), os.getcwd() + full_path)
            else:
                print(suc("Exporting:"), os.getcwd() + full_path)
                note_to_file(note, full_path)
                export_suc += 1
        if export_suc == len(notes):
            return Message("exported", suc("All selected notes exported."))
        elif export_suc == 0:
            return Message("exported", imp("Export failed, all files already exist."))
        else:
            return Message("exported", warn("Some notes not exported."))

    return Message("cancel", warn("Nothing changed."))


def cmd_last(args: list) -> Output:
    if len(args) > 0:
        if not args[0].isdigit() or int(args[0]) == 0:
            raise InvalidInput("last", args[0])
        selection: int = int(args[0])
    else:
        selection = 1
    result: list or None = select_last_note(selection)
    if result is None or len(result) == 0:
        raise MatchNotFound(f"last {selection} modified")
    return Listing(f"Last {selection} modified", add_tags_to_note(result))


# todo make ls <num> change how many notes shown per page
def cmd_list(args: list) -> Output:
    from cmd_accessories.list import dispatch
    if len(args) == 0:
        return Message("show")
    if args[0] not in dispatch.keys():
        raise NotListable(args[0])
    dispatch[args[0]]()
    return Message("hide")


# Entry-point for cmd_accessories called from dispatch table in Admin
def cmd_delete(notes: list, getconf=True) -> Output:
    if len(notes) == 0:
        raise SelectBeforeModify("delete.")

    def delete():
        tags: list = []
        for n in notes:
            if n.tags is not None and not n.tags.empty():
                tags = select_notetags(n.id)
                if tags:
                    tags = detuple(tags)
            delete_note(n.id, tags)
        return Message("deleted", suc("Note(s) deleted."))

    if getconf:
        if len(notes) == 1:
            print(imp('\nPERMANENTLY DELETING NOTE:'))
            notes[0].print_long()
        else:
            print(imp(f'\nPERMANENTLY DELETING {len(notes)} NOTES:'))
            for note in notes:
                note.print_tiny()
            print()

        if confirm("delete"):
            return delete()
        return Message("cancel", warn("Nothing deleted."))
    else:
        return delete()


def cmd_search(query: list) -> Output:
    if len(query) == 0:
        raise MissingSearchQuery("Search")
    result: list = select_like(query)
    if result is None or len(result) == 0:
        return Message("nomatch", warn(f"Match not found for `{' '.join(query)}`"))
    return Listing(f"Search for {' '.join(query)}", add_tags_to_note(result))


def cmd_merge(notes: list) -> Output:
    total_notes: int = len(notes)
    if total_notes == 0:
        return Message("cancel", imp("No notes provided to merge."))
    print(heading('\nMerging selected notes:'))
    print("  Concatenates all selected notes starting with first listed")
    print("  Notes will NOT be parsed for title or tags")
    print("  Creation date for merged note will be reset to today")

    print(f("\nMerge tags, too?", s='b') + f" Choose 'Y' to include tags in merger, 'n' to include NO tags.")
    do_merge_tags: bool = confirm("merge tags")
    print(f(imp("PERMANENTLY") + " delete originals?", s='i') + " Choose 'Y' to DELETE, 'n' to KEEP.")
    do_del_orig: bool = confirm("delete originals")
    print(f("Ready to merge?", s='b'))
    if not confirm("merge with chosen options"):
        return Message("cancel", warn("Merge cancelled."))

    new_date_norm = date_norm()
    new_note = Note(date_enc(), None, '', new_date_norm, new_date_norm, Tags(None))
    for ix, old_note in enumerate(notes):
        new_note.body += deparse_title(old_note.title) + old_note.body
        if ix != total_notes - 1:
            new_note.body += "\n===\n"

    if do_merge_tags:
        for old_note in notes:
            for tag in old_note.tags.tags:
                new_note.tags += tag

    if do_del_orig:
        cmd_delete(notes, getconf=False)

    save_note_and_tags(new_note)
    return Message("merged", suc("Notes merged."))
