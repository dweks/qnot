import textwrap
from util import date_obj, date_dif_today, MAX_WIDTH, line, gray


# TODO: inserting a note without a title to db gives title a value of "None" rather than a none-type. \
#  need a way to allow a user to use "None" as a title but still check for absence of a title
class Note:
    def __init__(self, pkey, title, body, date_c, date_m, tags):
        self.id = pkey
        self.title = title
        self.body = body
        self.date_c = date_c
        self.date_m = date_m
        self.tags = tags

    def print_oneline(self):
        trim = MAX_WIDTH - 8
        no_space = False
        # print("DIF:", date_dif_today(self.get_date_obj()))
        # print(self.date, end=' ')
        if self.title != "None":
            if len(self.title) > trim:
                print(self.oneline(self.title)[0:trim], end=gray('...\n'))
                no_space = True
            else:
                print(self.title, end=': ')
        trim -= len(self.title)
        if not no_space:
            if len(self.body) > trim:
                print(self.body.replace('\n', ' ')[0:trim], end=gray('...\n'))
            else:
                print(self.body.replace('\n', ' '))

    def print_multiline(self):
        SEP = max(len(self.title), len(self.body), len(self.date_c))
        SEP = MAX_WIDTH if SEP > MAX_WIDTH else SEP
        print(line(length=SEP))
        print(self.date_c)
        if self.title != "None":
            print(textwrap.fill(self.title, width=MAX_WIDTH))
        if len(self.body) > MAX_WIDTH:
            print(textwrap.fill(self.body, width=MAX_WIDTH))
        else:
            print(self.body)
        print(line(length=SEP))

    def get_date_obj(self):
        return date_obj(self.date_c)

    @staticmethod
    def oneline(string):
        return string.replace('\n', ' ')

    def __str__(self):
        return f"{self.id}, {self.title}, {self.body}, {self.date_c}, {self.date_m}"
