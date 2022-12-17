import math
from util import bld, lyel, debug
from exceptions import ListingItemNotExist, OutsidePageBounds, NoPagesInListing
from note import Note
ITEMS_PER_PAGE = 5


# TODO if select_notes_tagged_with returns None or just a string, must handle it before creating book
class Listing:

    def __init__(self, title, items):
        self.title = title
        self.items = items
        self.item_count = len(self.items)
        self.page_count = math.ceil(self.item_count / ITEMS_PER_PAGE)
        self.pages = self.generate()
        self.current_page = 1

    def generate(self) -> dict:
        pages = {}
        page_num = 1
        for i in range(0, self.item_count, ITEMS_PER_PAGE):
            pages[page_num] = [Note(*n) for n in self.items[i:i + ITEMS_PER_PAGE]]
            debug("generate")
            page_num += 1
        return pages

    def display_page(self):
        if self.page_count == 0:
            raise NoPagesInListing()

        print()
        print(bld(f"{self.title} -- found {self.item_count}"))
        for item in self.pages[self.current_page]:
            item_id = self.pages[self.current_page].index(item) + 1 + (self.current_page - 1) * ITEMS_PER_PAGE
            spacer = '  › ' if item_id < 10 else ' › ' if item_id < 100 else '› '
            print(item_id, end=spacer)
            item.print_oneline()
        print(bld("Page ") + lyel(f"{self.current_page} / {self.page_count}"))

    def next_page(self):
        if self.current_page + 1 > self.page_count:
            raise OutsidePageBounds(self.page_count)
        else:
            self.current_page += 1
            return True

    def prev_page(self):
        if self.current_page - 1 == 0:
            raise OutsidePageBounds(self.page_count)
        else:
            self.current_page -= 1
            return True

    def retrieve(self, index):
        if index - 1 < 0 or index > self.item_count:
            raise ListingItemNotExist(index)
        return self.pages[math.ceil(index / ITEMS_PER_PAGE)][(index - 1) % ITEMS_PER_PAGE]
