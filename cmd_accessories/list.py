from db_access import select_all_tags_and_count
from ut.disp import msg, bld, und, itl
from dispatch.adm import admin_dispatch
from dispatch.mod import mod_dispatch
from dispatch.std import std_dispatch
from dispatch.help import help_dispatch
# Lists things like commands, tags, help topics, etc


def list_tags():
    result = select_all_tags_and_count()
    print(msg("List of all used tags:"))
    printer([tag[0] for tag in result])
    print("Usage example (get notes by tag): " + bld("get <tag>"))


def list_help():
    print(msg("List of help topics (some are redundant):"))
    printer(list(help_dispatch.keys()))
    print("Usage: " + bld("help <topic>"))


def list_commands():
    print(msg("List of qnot commands (some are redundant):"))

    print(und("Admin mode:"))
    printer(list(admin_dispatch.keys()))
    print("Usage: " + bld("<command> [argument]\n"))

    print(und("Standard mode (from Linux):"))
    printer(list(std_dispatch.keys()))
    print("Usage: " + bld("qnot [command] [argument]\n"))

    print(und("Modify mode (after selecting note):"))
    printer(list(mod_dispatch.keys()))
    print("Usage: " + bld("<command>"))


def list_lists():
    print(msg("List of listable keywords (some are redundant):"))
    printer(list(dispatch.keys()))
    print("Usage: " + bld("[keyword]"))


def printer(lst: list):
    print(itl(' '.join(lst)))


dispatch = {
    'lists': list_lists,
    'list': list_lists,
    'ls': list_lists,
    'tags': list_tags,
    'tag': list_tags,
    'help': list_help,
    'commands': list_commands,
    'command': list_commands,
    'cmd': list_commands,
}

