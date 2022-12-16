from util import date_obj, date_dif_today


# TODO: inserting a note without a title to db gives title a value of "None" rather than a none-type. \
#  need a way to allow a user to use "None" as a title but still check for absence of a title
class Note:
    def __init__(self, pkey, title, body, tags, date):
        self.pkey = pkey
        self.title = title
        self.body = body
        self.tags = tags
        self.date = date

    def print_oneline(self):
        # print("DIF:", date_dif_today(self.get_date_obj()))
        # print(self.date, end=' ')
        if self.title != "None":
            print(self.title, end=': ')
        print(self.body.replace('\n', ' '))

    def print_multiline(self):
        print(self.date)
        if self.title != "None":
            print(self.title)
        print(self.body)
        print()

    def get_date_obj(self):
        return date_obj(self.date)

    def __str__(self):
        return f"{self.pkey}, {self.title}, {self.body}, {self.date}, {self.tags}"

