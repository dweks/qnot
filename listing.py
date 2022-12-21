import math
from ut.disp import msg, gray, lyel, bld
from exceptions import ListingItemNotExist, OutsidePageBounds, NoPagesInListing
from note import Note
ITEMS_PER_PAGE = 5


class Output:
    def __init__(self, source: str):
        self.source: str = source


# TODO if select_notes_tagged_with returns None or just a string, must handle it before creating book
class Listing(Output):
    def __init__(self, title: str or None, items: list, source: str):
        Output.__init__(self, source)
        self.title: str or None = title
        self.items: list = items
        self.item_count: int = len(self.items)
        self.page_count: int = math.ceil(self.item_count / ITEMS_PER_PAGE)
        self.pages: dict = self.generate()
        self.curr_pg: int = 1

    def generate(self) -> dict:
        pages: dict = {}
        page_num: int = 1
        for i in range(0, self.item_count, ITEMS_PER_PAGE):
            pages[page_num] = [Note(*n) for n in self.items[i:i + ITEMS_PER_PAGE]]
            page_num += 1
        return pages

    def display_page(self):
        if self.page_count == 0:
            raise NoPagesInListing()

        print(msg(f"\nListing `{self.title}` - found {self.item_count}"))
        for item in self.pages[self.curr_pg]:
            item_id: int = self.pages[self.curr_pg].index(item) + 1 + (self.curr_pg - 1) * ITEMS_PER_PAGE
            spacer: str = '  ┬ ' if item_id < 10 else ' ┬ ' if item_id < 100 else '┬ '
            print(lyel(str(item_id)), end=gray(spacer))
            item.print_trunc()
        print("PAGE " + bld(f"{self.curr_pg}") + gray(f" / {self.page_count}"))

    def next_page(self) -> bool:
        if self.curr_pg + 1 > self.page_count:
            raise OutsidePageBounds("last")
        else:
            self.curr_pg += 1
            return True

    def prev_page(self) -> bool:
        if self.curr_pg - 1 == 0:
            raise OutsidePageBounds("first")
        else:
            self.curr_pg -= 1
            return True

    def retrieve(self, index: int) -> Note:
        # todo need to redo this to accept ranges
        if index - 1 < 0 or index > self.item_count:
            raise ListingItemNotExist(index)
        return self.pages[math.ceil(index / ITEMS_PER_PAGE)][(index - 1) % ITEMS_PER_PAGE]


class Message(Output):
    def __init__(self, text: str, source: str):
        Output.__init__(self, source)
        self.text: str = text
        self.source: str = source

    def __eq__(self, other):
        return self.text == other
