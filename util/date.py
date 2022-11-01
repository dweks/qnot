import datetime as dt


# Date and time functions

# Encoded date
def date_enc():
    return dt.datetime.now().strftime(r"%m%d%y%H%M%S")


# Human-readable date
def date_norm():
    return dt.datetime.now().strftime(r"%x at %X")
