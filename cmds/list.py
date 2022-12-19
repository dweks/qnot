import dispatch as dsp
import ut
from db_access import select_all_tags_and_count
from exceptions import NotListable
from .help import help_dispatch


# Lists things like commands, tags, help topics, etc
def exec_list(args):
    if args is None:
        return "show"
    arg = args[0]

    if arg not in lists.keys():
        raise NotListable(arg)
    lists[arg]()
    return "suspend"


def list_tags():
    result = select_all_tags_and_count()
    print(ut.msg("List of all used tags:"))
    printer([tag[0] for tag in result])
    print("Usage example (get notes by tag): " + ut.bld("get <tag>"))


def list_help():
    print(ut.msg("List of help topics (some are redundant):"))
    printer(list(help_dispatch.keys()))
    print("Usage: " + ut.bld("help <topic>"))


def list_commands():
    print(ut.msg("List of qnot commands (some are redundant):"))

    print(ut.und("Admin mode:"))
    printer(list(dsp.admin_dispatch.keys()))
    print("Usage: " + ut.bld("<command> [argument]\n"))

    print(ut.und("Standard mode (from Linux):"))
    printer(list(dsp.std_dispatch.keys()))
    print("Usage: " + ut.bld("qnot [command] [argument]\n"))

    print(ut.und("Modify mode (after selecting note):"))
    printer(list(dsp.mod_dispatch.keys()))
    print("Usage: " + ut.bld("<command>"))


def list_lists():
    print(ut.msg("List of listable keywords (some are redundant):"))
    printer(list(lists.keys()))
    print("Usage: " + ut.bld("ls [keyword]"))


def printer(lst):
    print(ut.itl(' '.join(list(lst))))


lists = {
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
