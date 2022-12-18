import datetime as dt

DATE_AS_KEY = r"%m%d%y%H%M%S%f"
DATE_HUMAN_TIME = r"%x at %X"
DATE_HUMAN_NOTIME = r"%x"

# Date and time functions

# Encoded date
def date_enc():
    return dt.datetime.now().strftime(DATE_AS_KEY)


# Human-readable date
def date_norm():
    return dt.datetime.now().strftime(DATE_HUMAN_TIME)


# Turn date string into datetime object
def date_obj(string):
    return dt.datetime.strptime(string, DATE_HUMAN_TIME)


def date_dif_today(date):
    delta = date_obj(date_norm()) - date
    print(delta)
    print(delta.days)
    # print(delta.months)
    print(delta.minutes)
    print(delta.seconds)
    print(delta.microseconds)
