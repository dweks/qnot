import math
from ut.disp import msg, gray, lyel, line
from ut.prs import parse_slice
from exceptions import OutsidePageBounds, NoPagesInListing, InvalidRange
from notetags import Note
PAGE_MAX = 5


class Output:
    def __init__(self):
        pass


class Message(Output):
    def __init__(self, title: str, body: str = None):
        Output.__init__(self)
        self.title: str = title
        self.body: str = body

    def __eq__(self, other):
        return self.title == other

    def display(self):
        print(self.body)


# TODO if select_notes_tagged_with returns None or just a string, must handle it before creating book
class Listing(Output):
    def __init__(self, title: str or None, items: list, pp: int = PAGE_MAX):
        Output.__init__(self)
        self.title: str or None = title
        self.items: list = [Note(*n) for n in items]
        self.item_count: int = len(self.items)
        self.pp: int = pp
        self.page_count: int = math.ceil(self.item_count / pp)
        self.curr_pg: int = 1

    def display(self, tiny: bool = False, long: bool = False):
        if self.page_count == 0:
            raise NoPagesInListing()

        print(msg(f"\n{self.title}"))

        if long:
            for item in self.items:
                item.print_long()
        elif tiny:
            print(line())
            for item in self.items[(self.curr_pg - 1) * self.pp: min(self.curr_pg * self.pp, self.item_count)]:
                item_id: int = self.items.index(item) + 1
                spacer: str = '  ─ ' if item_id < 10 else ' ─ ' if item_id < 100 else '─ '
                print(lyel(str(item_id)), end=gray(spacer))
                item.print_tiny()
            print(line())

        else:
            for item in self.items[(self.curr_pg - 1) * self.pp: min(self.curr_pg * self.pp, self.item_count)]:
                item_id: int = self.items.index(item) + 1
                spacer: str = '  ┬ ' if item_id < 10 else ' ┬ ' if item_id < 100 else '┬ '
                print(lyel(str(item_id)), end=gray(spacer))
                item.print_short()
        print(f"{'Notes: '+ msg(str(self.item_count))}", end='')
        print(gray(' | '), end='')
        print(f"PAGE {self.curr_pg}/{self.page_count}", end='')
        if 1 < self.page_count < 10:
            print(gray(' | '), end='')
            for i in range(1, self.page_count + 1):
                if i == self.curr_pg:
                    print(lyel(str(i)), end='  ')
                else:
                    print(gray(str(i)), end='  ')
        print()

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

    def retrieve(self, sel: str) -> list:
        sel_slice: slice = slice(int(sel)-1, int(sel)) if len(sel) == 1 else parse_slice(sel)
        if sel_slice is None or sel_slice.start < 0 or sel_slice.stop > self.item_count:
            raise InvalidRange(self.item_count)
        return [(i.id, i.title, i.body, i.date_c, i.date_m, i.tags) for i in self.items[sel_slice]]
