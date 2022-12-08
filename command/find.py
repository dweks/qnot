from db_access import select_notes_tagged_with as select_by_tag
from book import Book


# Entry-point for command called from dispatch table in Admin
# Find will search the notes in the database for a provided string.
# This command can be called with optional parameters 'filter' and 'section'
# which alter the generation of SQL queries. If 'find' is not provided with
# a filter or section and only a search string, the default searched location
# is TODO
def exec_find(args) -> Book or str:
    filters = {'last', 'today', 'week', 'day', }
    section = {'title', 'body', 'tag', }
    filt, sect, query = None, None, None
    length = len(args) if args is not None else 0

    if not args or length == 0:
        return "Command 'find' must take arguments or a search query."

    if length == 1:
        if args[0] in filters or args[0] in section:
            return "Provide a search query."

    if args[0] in filters:
        filt = args[0]
        if args[1] in section:
            sect = args[1]
            query = args[2:]
            # return f"Provide arguments for {args[1]}"
        else:
            query = args[1:]
    elif args[0] in section:
        sect = args[0]
        query = args[1:]
    else:
        query = args

    if not query:
        return "Provide a search query."

    result = select(filt, sect, query)
    if not result:
        return "No match"
    return Book(result)


def select(filt, sect, query) -> list or str:
    # If no filter, default to tag search
    if not filt and not sect:
        return select_by_tag(query)
