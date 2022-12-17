from db_access import select_notes_tagged_with as select_by_tag
from listing import Listing
from exceptions import MissingArguments, MissingSearchQuery, MatchNotFound
from util import debug


# Entry-point for cmds called from dispatch table in Admin
# Find will search the notes in the database for a provided string.
# This cmds can be called with optional parameters 'filter' and 'section'
# which alter the generation of SQL queries. If 'find' is not provided with
# a filter or section and only a search string, the default searched location
# is TODO
def exec_find(args):
    filters = {'today', 'week', 'day', }
    section = {'title', 'body', 'tag', }
    filt, sect, query = None, None, None
    length = len(args) if args is not None else 0

    if not args or length == 0:
        raise MissingArguments("find")

    if length == 1:
        if args[0] in filters or args[0] in section:
            raise MissingSearchQuery(f"find {args[0]}")

    if args[0] in filters:
        filt = args[0]
        if args[1] in section:
            sect = args[1]
            query = args[2:]
        else:
            query = args[1:]
    elif args[0] in section:
        sect = args[0]
        query = args[1:]
    else:
        query = args

    if not query:
        raise MissingSearchQuery(f"find {args[0]}")

    result = select(filt, sect, query)
    if result is None or len(result) == 0:
        raise MatchNotFound(' '.join(args))
    # TODO: change 'matching tag' to be dynamic
    return Listing(f"Matching tag: {' '.join(args)}", result)


def select(filt, sect, query) -> list or str:
    # If no filter, default to tag search
    if not filt and not sect:
        return select_by_tag(query)
