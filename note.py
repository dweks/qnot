from ut.disp import MAX_WIDTH, gray, und, bld, itl, line
from ut.date import date_obj


# TODO: inserting a note withoa title to db gives title a value of "None" rather than a none-type. \
#  need a way to allow a user to use "None" as a title bstill check for absence of a title
class Note:
    def __init__(self, pkey, title, body, date_c, date_m, tags):
        self.id = pkey
        self.title = title
        self.body = body
        self.date_c = date_c
        self.date_m = date_m
        self.tags = tags

    def print_trunc(self):
        trim = MAX_WIDTH - 11
        no_space = False
        mid = gray('   │ ')
        end = gray('   └ ')
        # print("DIF:", date_dif_today(self.get_date_obj()))
        date = self.get_date_obj()
        date = str(date.month) + '/' + str(date.day) + '/' + str(date.year)

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
        if self.tags is not None:
            # todo tags not printing
            print(end + gray(', '.join(self.tags)))
        else:
            print(end + gray("notag"))
        print()

    # todo: print time as just hour:mins
    def print_full(self):
        # comp space for printing
        if self.title is not None and self.title != "None":
            SEP = max(len(self.title), len(self.body), len(self.date_c))
        else:
            SEP = max(len(self.body), len(self.date_c))
        SEP = (MAX_WIDTH if SEP > MAX_WIDTH else SEP) + 10

        print(line(length=SEP))

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
        if self.tags:
            print(gray(itl(', '.join(self.tags))))
        else:
            print(gray(itl("notag")))

        print(line(length=SEP))

    def get_date_obj(self):
        return date_obj(self.date_c)

    @staticmethod
    def oneline(string):
        return string.replace('\n', ' ')

    def __str__(self):
        return f"{self.id}, {self.title}, {self.body}, {self.date_c}, {self.date_m}"
