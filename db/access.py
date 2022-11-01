import sqlite3 as sql

# Paths and filenames
DB_PATH = ".notes.db"

# Table column names
NOTES_COL_PKEY = "id"
NOTES_COL_TITLE = "title"
NOTES_COL_BODY = "body"
NOTES_COL_TAGS = "tags"
NOTES_COL_DATE = "date"
TAGS_COL_TAG = "tag"


def db_connect():
    try:
        db_connection = sql.connect(DB_PATH)
        return db_connection
    except sql.Error as e:
        print(f"Database connection error ({db_connect.__name__}):", e)


def db_init():
    create_table_notes = \
        f""" 
        CREATE TABLE IF NOT EXISTS Notes (
            {NOTES_COL_PKEY}    TEXT    PRIMARY KEY,
            {NOTES_COL_TITLE}   TEXT    DEFAULT NULL,
            {NOTES_COL_BODY}    TEXT    NOT NULL,
            {NOTES_COL_DATE}    TEXT    DEFAULT NULL
            {NOTES_COL_TAGS}    TEXT    DEFAULT NULL
        );
        """
    create_table_tags = \
        f""" 
        CREATE TABLE IF NOT EXISTS Tags (
            {TAGS_COL_TAG}      TEXT    PRIMARY KEY
        );
        """

    try:
        with db_connect() as dbc:
            dbc.cursor().execute(create_table_notes)
            dbc.cursor().execute(create_table_tags)
    except sql.Error as e:
        print(f"Database initialization error ({db_init.__name__}):", e)
