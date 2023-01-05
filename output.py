import math
from ut.disp import gry, heading, f
from ut.prs import parse_selection
from exceptions import OutsidePageBounds, NoPagesInListing, InvalidSelection
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

        print(heading(self.title))

        if long:
            for item in self.items:
                item.print_long()
        elif tiny:
            for item in self.items[(self.curr_pg - 1) * self.pp: min(self.curr_pg * self.pp, self.item_count)]:
                print(gry('∙'), end=' ')
                item.print_tiny()
            print()
        else:
            for item in self.items[(self.curr_pg - 1) * self.pp: min(self.curr_pg * self.pp, self.item_count)]:
                item_id: int = self.items.index(item) + 1
                spacer: str = '  ┬ ' if item_id < 10 else ' ┬ ' if item_id < 100 else '┬ '
                print(f(str(item_id), 'ly'), end=gry(spacer))
                item.print_short()
        print(f"{'Notes: '+ f(str(self.item_count),'y','b')}", end='')
        print(gry(' | '), end='')
        print(f"PAGE {self.curr_pg}/{self.page_count}", end='')
        if 1 < self.page_count < 10:
            print(gry(' | '), end='')
            for i in range(1, self.page_count + 1):
                if i == self.curr_pg:
                    print(f(str(i), 'lm'), end='  ')
                else:
                    print(gry(str(i)), end='  ')
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

    def retrieve(self, sel: list) -> list:
        selection: list = []
        if len(sel) == 1 and sel[0] == "all":
            return [n.select() for n in self.items]
        elif "all" in sel:
            raise InvalidSelection(' '.join(sel))

        slc, sng = parse_selection(sel)
        if len(slc) > 0:
            for s in slc:
                if s.start < 0 or s.stop > self.item_count:
                    raise InvalidSelection(' '.join(sel))
                for n in self.items[s]:
                    selection.append(n.select())
        if len(sng) > 0:
            for s in sng:
                if s < 0 or s >= self.item_count:
                    raise InvalidSelection(' '.join(sel))
                if self.items[s].select() not in selection:
                    selection.append(self.items[s].select())
        return list(selection)
