import math
from note import Note
NOTES_PER_PAGE = 5


# TODO if select_notes_tagged_with returns None or just a string, must handle it before creating book
class Book:
    def __init__(self, notes):
        self.notes = notes
        self.note_count = len(self.notes)
        self.page_count = math.ceil(self.note_count / NOTES_PER_PAGE)
        self.pages = self.generate()

    def generate(self) -> dict:
        pages = {}
        page_num = 1
        for i in range(0, self.note_count, NOTES_PER_PAGE):
            pages[page_num] = [Note(*n) for n in self.notes[i:i + NOTES_PER_PAGE]]
            page_num += 1
        return pages
