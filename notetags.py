import datetime as dt
from ut.disp import MAX_WIDTH, gray, und, bld, line
from ut.date import date_obj

NOTAG: str = "untagged"


class Tags:
    def __init__(self, tags: list or None = None):
        self.tags: set = set()
        if tags is None or len(tags) == 0:
            self.tags.add(NOTAG)
        else:
            self.tags = set(tags)

    def empty(self) -> bool:
        return len(self.tags) == 1 and NOTAG in self.tags

    def str(self) -> str:
        return ', '.join(self.tags)

    def __iadd__(self, new_tags: list):
        self.tags.update(new_tags)
        if len(self.tags) > 1 and NOTAG in self.tags:
            self.tags.remove(NOTAG)
        return self


# TODO: inserting a note withoa title to db gives title a value of "None" rather than a none-type. \
#  need a way to allow a user to use "None" as a title bstill check for absence of a title
class Note:
    def __init__(self, pk: str, title: str or None, body: str, date_c: str, date_m: str, tags: Tags):
        self.id: str = pk
        self.title: str = title
        self.body: str = body
        self.date_c: str = date_c
        self.date_m: str = date_m
        self.tags: Tags = tags

    def print_tiny(self):
        trim: int = MAX_WIDTH - 11
        no_space: bool = False
        if self.title != "None" and self.title is not None:
            if len(self.title) + 2 > trim:
                print(und(bld(self.oneline(self.title)[0:trim])), end=gray('...\n'))
                no_space = True
            else:
                print(und(bld(self.title)), end=': ')
                trim -= 2
            trim -= len(self.title)
        if not no_space:
            if len(self.oneline(self.body)) > trim:
                print(self.oneline(self.body)[0:trim], end=gray('...\n'))
            else:
                print(self.oneline(self.body[0:trim]))

    def print_short(self):
        trim: int = MAX_WIDTH - 11
        no_space: bool = False
        mid: str = gray('   │ ')
        end: str = gray('   └ ')
        # print("DIF:", date_dif_today(self.get_date_obj()))
        date: dt.datetime = self.get_date_obj()
        date: str = str(date.month) + '/' + str(date.day) + '/' + str(date.year)

        # title
        if self.title != "None" and self.title is not None:
            if len(self.title) + 2 > trim:
                print(und(bld(self.oneline(self.title)[0:trim])), end=gray('...\n'))
                no_space = True
            else:
                print(und(bld(self.title)), end=': ')
                trim -= 2
            trim -= len(self.title)
        # note
        if not no_space:
            if len(self.oneline(self.body)) > trim:
                print(bld(self.oneline(self.body)[0:trim]), end=gray('...\n'))
            else:
                print(bld(self.oneline(self.body[0:trim])))
        # todo: when showing last modified, show date as mod date
        # date / tags
        print(mid + date)
        print(end + gray(self.tags.str()))
        print()

    # todo: print time as just hour:mins
    def print_long(self):
        # comp space for printing
        if self.title is not None and self.title != "None":
            width: int = max(len(self.title), len(self.body), len(self.date_c))
        else:
            width = max(len(self.body), len(self.date_c))
        width = (MAX_WIDTH if width > MAX_WIDTH else width) + 10

        print(line(length=width))

        # title/body
        if self.title is not None and self.title != "None":
            print(und(self.title))
        if len(self.body) > MAX_WIDTH:
            print(bld(self.body))
        else:
            print(bld(self.body))

        # todo: rethink how tags are printed
        # date/tags
        print(line(length=5))
        print("Created: " + self.date_c)
        print("Modified: " + self.date_m)
        print(gray(self.tags.str()))

        print(line(length=width))

    def get_date_obj(self) -> dt.datetime:
        return date_obj(self.date_c)

    @staticmethod
    def oneline(text) -> str:
        return text.replace('\n', ' ')

    def select(self) -> tuple:
        return self.id, self.title, self.body, self.date_c, self.date_m, self.tags

    def __str__(self):
        return f"{self.id}, {self.title}, {self.body}, {self.date_c}, {self.date_m}"
