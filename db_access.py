import sqlite3 as SQL
from exceptions import MissingArguments, MatchNotFound

# Paths and filenames
DB_PATH = ".notes.db"

# Table column names
NOTES_COL_PKEY = "id"
NOTES_COL_TITLE = "title"
NOTES_COL_BODY = "body"
NOTES_COL_TAGS = "tags"
NOTES_COL_DATE = "date"
TAGS_COL_TAG = "tag"
TAG_COL_NOTE = "note"

PREPEND = "t_"


def ex(sql, source, params=None, fetch=False, commit=False):
    try:
        with SQL.connect(DB_PATH) as dbc:
            if params is not None:
                res = dbc.cursor().execute(sql, params)
            else:
                res = dbc.cursor().execute(sql)
            if commit:
                dbc.commit()
            elif fetch:
                res = res.fetchall()

    except SQL.Error as e:
        print(f"Problem in db.{source}:")
        print(e)
        res = None
    return res


def db_init():
    sql = "PRAGMA foreign_keys = ON"
    ex(sql, db_init.__name__)
    create_tags_table()
    create_notes_table()
    insert_default_tags()


def insert_default_tags():
    sql = f"INSERT OR IGNORE INTO Tags ({TAGS_COL_TAG}) VALUES ( 'notag' );"
    ex(sql, insert_default_tags.__name__)
    create_tag_table("notag")


def create_notes_table():
    sql = \
        f""" 
        CREATE TABLE IF NOT EXISTS Notes (
            {NOTES_COL_PKEY}    TEXT    PRIMARY KEY,
            {NOTES_COL_TITLE}   TEXT    DEFAULT NULL,
            {NOTES_COL_BODY}    TEXT    NOT NULL,
            {NOTES_COL_TAGS}    TEXT    DEFAULT NULL,
            {NOTES_COL_DATE}    TEXT    NOT NULL
        );
        """
    ex(sql, create_notes_table.__name__)


def create_tags_table():
    sql = \
        f""" 
        CREATE TABLE IF NOT EXISTS Tags (
            {TAGS_COL_TAG}      TEXT    PRIMARY KEY
        );
        """
    ex(sql, create_tags_table.__name__)


def create_tag_table(tag):
    sql = \
        f""" 
        CREATE TABLE IF NOT EXISTS {PREPEND + tag} (
            {TAG_COL_NOTE}      TEXT    NOT NULL
        );
        """
    ex(sql, create_tag_table.__name__)


def tag_exists(tag):
    sql = f"SELECT * FROM Tags WHERE tag = ?;"
    return ex(sql, tag_exists.__name__, params=[tag], fetch=True)


def insert_note_to_notes(note):
    sql = \
        f"""
        INSERT INTO Notes (
            {NOTES_COL_PKEY},
            {NOTES_COL_TITLE},
            {NOTES_COL_BODY},
            {NOTES_COL_TAGS},
            {NOTES_COL_DATE}
        ) VALUES (
            "{note.pkey}",
            "{note.title}",
            "{note.body}",
            "{note.tags}",
            "{note.date}"
        );
        """
    ex(sql, insert_note_to_notes.__name__)


# Inserts a single unique tag to table of all tags
def insert_tag_to_tags(tag):
    sql = f" INSERT OR IGNORE INTO Tags ( {TAGS_COL_TAG} ) VALUES ( ? );"
    ex(sql, insert_tag_to_tags.__name__, params=[tag])


def insert_note_to_tag(tag, note_id):
    sql = f"INSERT OR IGNORE INTO {PREPEND + tag} ({TAG_COL_NOTE}) VALUES ( ? );"
    ex(sql, insert_note_to_tag.__name__, params=[note_id])


# Returns a list of tuples (even if only one found)
def select_notes_tagged_with(tags) -> list or str:
    if tags is None or len(tags) == 0:
        raise MissingArguments(select_notes_tagged_with.__name__)
    for tag in tags:
        t = tag_exists(tag)
        if t is None or len(t) == 0:
            raise MatchNotFound(', '.join(tags))
    sql = \
        f"""
        SELECT
            {NOTES_COL_PKEY},
            {NOTES_COL_TITLE},
            {NOTES_COL_BODY},
            {NOTES_COL_TAGS},
            {NOTES_COL_DATE}
        FROM Notes
        """
    for tag in tags:
        sql += f" JOIN {PREPEND + tag} ON {PREPEND + tag}.note = Notes.id"
    sql += ';'

    return ex(sql, select_notes_tagged_with.__name__, fetch=True)


def remove_note(note):
    if not note:
        raise MissingArguments({remove_note.__name__})
    sql = f"DELETE FROM Notes WHERE {NOTES_COL_PKEY} = ?;"
    ex(sql, remove_note.__name__, params=[note.pkey], commit=True)
    remove_note_from_tag(note.pkey, note.tags)


def remove_note_from_tag(note_id, tags):
    if not note_id:
        raise MissingArguments({remove_note_from_tag.__name__})
    sql = ''
    # TODO why is this a string and not a list?
    for tag in tags:
        sql = f"DELETE FROM {tag} WHERE {TAG_COL_NOTE} = ?;"
    ex(sql, remove_note_from_tag.__name__, params=[note_id], commit=True)


def select_all_tags():
    sql = "SELECT tag FROM Tags;"
    return ex(sql, select_all_tags.__name__, fetch=True)


def select_last(num):
    sql = "SELECT * FROM Notes ORDER BY ROWID DESC LIMIT ?;"
    return ex(sql, select_last.__name__, params=[num], fetch=True)
