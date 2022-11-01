from output import Output
from db.access import db_connect


# Entry-point for command called from dispatch table in Admin
# Find will search the notes in the database for a provided string.
# This command can be called with optional parameters 'filter' and 'section'
# which alter the generation of SQL queries. If 'find' is not provided with
# a filter or section and only a search string, the default searched location
# is TODO
def exec_find(args):

    filt = {
        'last',
        'today',
        'week',
        'day',
    }

    section = {
        'title',
        'body',
        'tag',
    }

    fcmd, sect, query = None, None, None
    if len(args) == 0:
        raise IOError("Command 'find' must take args.")

    if args[0] in filt:
        fcmd = args[0]
        if args[1] in section:
            sect = args[1]
        if args[2]:
            query = args[2:]
    elif args[0] in section:
        sect = args[0]
        if args[1]:
            query = args[1]

    select(fcmd, sect, query)


def select(filt, sect, query):
    if not query:
        raise IOError("Command 'find' must have a search query.")

    if not filt and not sect:
        sql_cmd = """
        SELECT title, body FROM Notes WHERE tags = ?"
        """
    sq_cmd = """
        SELECT * FROM Notes WHERE title = ? AND body = ?;
    """

    with db_connect() as dbc:
        cursor = dbc.cursor()
        cursor.execute(sq_cmd, params)
        result = cursor.fetchall()


def f_last():
    pass


def f_today():
    pass


def f_week():
    pass


def f_day():
    pass
