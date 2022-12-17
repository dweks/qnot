import textwrap
from util import line, itl
import json
from util import date_obj, date_dif_today, MAX_WIDTH


# TODO: inserting a note without a title to db gives title a value of "None" rather than a none-type. \
#  need a way to allow a user to use "None" as a title but still check for absence of a title
class Note:
    def __init__(self, pkey, title, body, tags, date):
        self.pkey = pkey
        self.title = title
        self.body = body
        self.tags = eval(tags)
        print(type(tags))
        print(tags)
        self.date = date

    def print_oneline(self):
        neg = 3 + len(self.title) + 2
        # print("DIF:", date_dif_today(self.get_date_obj()))
        # print(self.date, end=' ')
        if self.title != "None":
            print(self.title, end=': ')
        if len(self.body) > MAX_WIDTH - neg:
            print(self.body.replace('\n', ' ')[0:MAX_WIDTH - neg], end='...\n')
        else:
            print(self.body.replace('\n', ' '))

    def print_multiline(self):
        print(line())
        print(self.date)
        if self.title != "None":
            print(self.title)
        if len(self.body) > MAX_WIDTH:
            print(textwrap.fill(self.body, width=MAX_WIDTH))
        else:
            print(self.body)
        if len(self.tags) > 0:
            print(itl(f"Tagged with: {', '.join(self.tags)}"))
        print(line())

    def get_date_obj(self):
        return date_obj(self.date)

    def __str__(self):
        return f"{self.pkey}, {self.title}, {self.body}, {self.date}, {self.tags}"

