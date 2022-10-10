class Note:
    data = dict(date=None, title=None, note=None, tags=None)

    def __init__(self, date, title, note, tags):
        self.data["date"] = date
        self.data["title"] = title
        self.data["note"] = note
        self.data["tags"] = tags
