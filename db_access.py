import sqlite3 as sql
from note import Note

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


def curs(source):
    try:
        with connect() as dbc:
            return dbc.cursor()
    except sql.Error as e:
        print(source, e)


def connect():
    try:
        conn = sql.connect(DB_PATH)
        return conn
    except sql.Error as e:
        print(f"Database connection error ({connect.__name__}):", e)


def db_init():
    connect().cursor().execute("PRAGMA foreign_keys = ON")
    create_tags_table()
    create_notes_table()


def create_notes_table():
    table = \
        f""" 
        CREATE TABLE IF NOT EXISTS Notes (
            {NOTES_COL_PKEY}    TEXT    PRIMARY KEY,
            {NOTES_COL_TITLE}   TEXT    DEFAULT NULL,
            {NOTES_COL_BODY}    TEXT    NOT NULL,
            {NOTES_COL_DATE}    TEXT    NOT NULL,
            {NOTES_COL_TAGS}    TEXT    DEFAULT NULL
        );
        """
    try:
        with connect() as dbc:
            dbc.cursor().execute(table)
    except sql.Error as e:
        print(f"Database initialization error ({create_notes_table.__name__}):", e)


def create_tags_table():
    table = \
        f""" 
        CREATE TABLE IF NOT EXISTS Tags (
            {TAGS_COL_TAG}      TEXT    PRIMARY KEY
        );
        """

    try:
        with connect() as dbc:
            dbc.cursor().execute(table)
    except sql.Error as e:
        print(f"Database initialization error ({create_tags_table.__name__}):", e)


def create_tag_table(tag):
    table = \
        f""" 
        CREATE TABLE IF NOT EXISTS {tag} (
            {TAG_COL_NOTE}      TEXT    NOT NULL
        );
        """
    try:
        with connect() as dbc:
            dbc.cursor().execute(table)
    except sql.Error as e:
        print(f"Database initialization error ({create_tags_table.__name__}):", e)


def tag_exists(tag):
    selection = \
        f"""
        SELECT * FROM Tags WHERE tag = ?;
        """
    try:
        with connect() as dbc:
            cursor = dbc.cursor().execute(selection, [tag])
            return cursor.fetchall()

    except sql.Error as e:
        print(f"Problem selecting tag in {tag_exists.__name__}: ", e)


def insert_note_to_notes(note):
    insertion = \
        f"""
        INSERT INTO Notes (
            {NOTES_COL_PKEY},
            {NOTES_COL_TITLE},
            {NOTES_COL_BODY},
            {NOTES_COL_DATE},
            {NOTES_COL_TAGS}
        ) VALUES (
            "{note.pkey}",
            "{note.title}",
            "{note.body}",
            "{note.date}",
            "{note.tags}"
        );
        """
    try:
        with connect() as dbc:
            dbc.cursor().execute(insertion)

    except sql.Error as e:
        print(insert_note_to_notes.__name__, e)


# Inserts a single unique tag to table of all tags
def insert_tag_to_tags(tag):
    insertion = \
        f"""
        INSERT OR IGNORE INTO Tags ( {TAGS_COL_TAG} ) VALUES ( ? );
        """
    try:
        with connect() as dbc:
            dbc.cursor().execute(insertion, [tag])

    except sql.Error as e:
        print(insert_tag_to_tags.__name__, e)


def insert_note_to_tag(tag, note_id):
    insertion = \
        f"""
        INSERT OR IGNORE INTO {tag} ({TAG_COL_NOTE}) VALUES ( ? );
        """
    try:
        with connect() as dbc:
            dbc.cursor().execute(insertion, [note_id])

    except sql.Error as e:
        print(insert_tag_to_tags.__name__, e)


# Returns a list of tuples (even if only one found)
def select_notes_tagged_with(tags) -> list or str:
    if len(tags) == 0:
        return "Must enter tags to search for."
    selection = "SELECT id, title, body, tags, date FROM Notes"
    for tag in tags:
        selection += f" JOIN {tag} ON {tag}.note = Notes.id"
    selection += ';'

    try:
        c = curs(select_notes_tagged_with.__name__)
        res = c.execute(selection).fetchall()
    except sql.Error:
        res = None

    return res
