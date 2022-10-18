class Note:
    def __init__(self, title, note, tags, path, date):
        self.__title = title
        self.__note = note
        self.__tags = tags
        self.__path = path
        self.__date = date

    def dump(self):
        return {
            "title": self.__title,
            "note": self.__note,
            "tags": self.__tags
        }

    def get_title_note(self):
        # TODO consider adding formatting argument options
        return self.__title + r" :: " + self.__note

    def get_tags(self):
        return self.__tags

    def get_title(self):
        return self.__title

    def get_note(self):
        return self.__note

    def set_note(self, new_note):
        self.__note = new_note

    def set_title(self, new_title):
        self.__title = new_title

    def get_path(self, part=0):
        return self.__path

