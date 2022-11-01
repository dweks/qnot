import db.access as db


def ins_note(note):
    insertion = \
        f"""
        INSERT INTO Notes (
            {db.NOTES_COL_PKEY},
            {db.NOTES_COL_TITLE},
            {db.NOTES_COL_BODY},
            {db.NOTES_COL_DATE},
            {db.NOTES_COL_TAGS}
        ) VALUES (
            "{note["pkey"]}"
            "{note["title"]}",
            "{note["body"]}",
            "{note["date"]}",
            "{note["tags"]}"
        )
        """
    try:
        with db.db_connect() as dbc:
            dbc.cursor().execute(insertion)

    except db.sql.Error as e:
        print(ins_note.__name__, e)


# Inserts a single unique tag to table of all tags
def ins_tag_row(tag):
    insertion = \
        f"""
        INSERT OR IGNORE INTO Tags (
            {db.TAGS_COL_TAG} 
        ) VALUES ( 
            "{tag}" 
        )
        """
    try:
        with db.db_connect() as dbc:
            dbc.cursor().execute(insertion)

    except db.sql.Error as e:
        print(ins_tag_row.__name__, e)
