import sqlite3 as sql
from file import DB_FULL


def db_init():
    create_table_notes = \
        """ 
        CREATE TABLE IF NOT EXISTS Notes (
            id      INTEGER     PRIMARY KEY,
            title   TEXT,
            note    TEXT        NOT NULL,
            tags    TEXT,
            date    TEXT        NOT NULL
        );
        """
    create_table_tags = \
        """ 
        CREATE TABLE IF NOT EXISTS Tags (
            tag      text     PRIMARY KEY
        );
        """

    try:
        create_table(create_table_notes)
        create_table(create_table_tags)
    except sql.Error as e:
        print("db_init() :", e)


def db_connect():
    connection = None
    try:
        connection = sql.connect(DB_FULL)
    except sql.Error as e:
        print("database error:", e)
    return connection


def create_table(create_table_sql):
    dbc = db_connect()
    dbc.cursor().execute(create_table_sql)
    dbc.close()
