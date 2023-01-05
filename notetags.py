import datetime as dt
from ut.disp import MAX_WIDTH, line, f, gry
from ut.date import date_obj

NOTAG: str = "untagged"


class Tags:
    def __init__(self, tags: list or None = None):
        self.tags: set = set()
        if tags is None or len(tags) == 0:
            self.tags.add(NOTAG)
        else:
            tags.sort(key=str)
            self.tags = set(tags)

    def empty(self) -> bool:
        return len(self.tags) == 1 and NOTAG in self.tags

    def str(self) -> str:
        return ', '.join(self.tags)

    def __iadd__(self, new_tags: list or str):
        self.tags.update(new_tags if type(new_tags) == list else [new_tags])
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
                print(f(self.oneline(self.title)[0:trim], s='bu'), end=gry('...\n',))
                no_space = True
            else:
                print(f(self.title, s='bu'), end=': ')
                trim -= 2
            trim -= len(self.title)
        if not no_space:
            if len(self.oneline(self.body)) > trim:
                print(self.oneline(self.body)[0:trim], end=gry('...\n'))
            else:
                print(self.oneline(self.body[0:trim]))

    def print_short(self):
        trim: int = MAX_WIDTH - 11
        no_space: bool = False
        mid: str = gry('   │ ')
        end: str = gry('   └ ')
        # print("DIF:", date_dif_today(self.get_date_obj()))
        date: dt.datetime = self.get_datec_obj()
        date: str = str(date.month) + '/' + str(date.day) + '/' + str(date.year)

        # title
        if self.title != "None" and self.title is not None:
            if len(self.title) + 2 > trim:
                print(f(self.oneline(self.title)[0:trim], s='bu'), end=gry('...\n'))
                no_space = True
            else:
                print(f(self.title, s='bu'), end=': ')
                trim -= 2
            trim -= len(self.title)
        # note
        if not no_space:
            if len(self.oneline(self.body)) > trim:
                print(f(self.oneline(self.body)[0:trim], s='b'), end=gry('...\n'))
            else:
                print(f(self.oneline(self.body[0:trim]), s='b'))
        # todo: when showing last modified, show date as mod date
        # date / tags
        print(mid + f(self.tags.str(), 'lb'))
        print(end + gry(date))
        print()

    # todo: print time as just hour:mins
    def print_long(self):
        print(line(char='=', length=30))

        # title/body
        if self.title is not None and self.title != "None":
            print(f(self.title, s='u'))
        print(f(self.body, s='b'))

        # todo: rethink how tags are printed
        # date/tags
        print(line(length=5))
        print(f(self.tags.str(), 'lb'))
        print(gry("Created: " + self.date_c))
        print(gry("Modified: " + self.date_m))

        print(line(char='=', length=30))

    def get_datec_obj(self) -> dt.datetime:
        return date_obj(self.date_c)

    def get_datem_obj(self) -> dt.datetime:
        return date_obj(self.date_m)

    @staticmethod
    def oneline(text) -> str:
        return text.replace('\n', ' ')

    def select(self) -> tuple:
        return self.id, self.title, self.body, self.date_c, self.date_m, self.tags

    def __str__(self):
        return f"{self.id}, {self.title}, {self.body}, {self.date_c}, {self.date_m}"
