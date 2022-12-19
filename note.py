import textwrap
import ut as ut


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

    def print_trunc(self):
        trim = ut.MAX_WIDTH - 8
        no_space = False
        mid = ut.gray('   │ ')
        end = ut.gray('   └ ')
        # print("DIF:", date_dif_today(self.get_date_obj()))
        date = self.get_date_obj()
        date = str(date.month) + '/' + str(date.day) + '/' + str(date.year)

        # title
        if self.title != "None" and self.title is not None:
            if len(self.title) > trim:
                print(ut.bld(self.oneline(self.title)[0:trim]), end=ut.gray(' ...\n'))
                no_space = True
            else:
                print(ut.bld(self.title), end=': ')
            trim -= len(self.title)
        # note
        if not no_space:
            if len(self.body) > trim:
                print(ut.bld(self.body.replace('\n', ' ')[0:trim]), end=ut.gray(' ...\n'))
            else:
                print(ut.bld(self.body.replace('\n', ' ')))
        # date / tags
        print(mid + date)
        if self.tags is not None:
            # todo tags not printing
            print(end + ut.gray(', '.join(self.tags)))
        else:
            print(end + ut.gray("notag"))
        print()

    def print_full(self):
        # compute space for printing
        if self.title is not None and self.title != "None":
            SEP = max(len(self.title), len(self.body), len(self.date_c))
        else:
            SEP = max(len(self.body), len(self.date_c))
        SEP = ut.MAX_WIDTH if SEP > ut.MAX_WIDTH else SEP

        print(ut.line(length=SEP))

        # title/body
        if self.title is not None and self.title != "None":
            print(ut.und(textwrap.fill(self.title, width=ut.MAX_WIDTH, replace_whitespace=False)))
        if len(self.body) > ut.MAX_WIDTH:
            print(ut.bld(textwrap.fill(self.body, width=ut.MAX_WIDTH, replace_whitespace=False)))
        else:
            print(ut.bld(self.body))

        # date/tags
        print(self.date_c)
        if self.tags:
            print(ut.gray(ut.itl(', '.join(self.tags))))
        else:
            print(ut.gray(ut.itl("notag")))

        print(ut.line(length=SEP))

    def get_date_obj(self):
        return ut.date_obj(self.date_c)

    @staticmethod
    def oneline(string):
        return string.replace('\n', ' ')

    def __str__(self):
        return f"{self.id}, {self.title}, {self.body}, {self.date_c}, {self.date_m}"
