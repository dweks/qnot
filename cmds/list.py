from db_access import select_all_tags
from exceptions import MissingArguments, NotListable
from util import msg

# Lists things like commands, tags, help topics, etc
def exec_list(args):
    if args is None:
        return "show"
    arg = args[0]
    lists = {
        'tags': select_all_tags,
    }

    if arg not in lists.keys():
        raise NotListable(arg)
    print(msg(f"Listing all {arg}"))
    print(', '.join(elm[0] for elm in lists[arg]()))

    return "suspend"
