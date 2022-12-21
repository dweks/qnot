import datetime as dt

DATE_AS_KEY = r"%y%m%d%H%M%S%f"
DATE_HUMAN_TIME = r"%x at %X"
DATE_HUMAN_NOTIME = r"%x"


# Encoded date
def date_enc() -> str:
    return dt.datetime.now().strftime(DATE_AS_KEY)


# Human-readable date
def date_norm() -> str:
    return dt.datetime.now().strftime(DATE_HUMAN_TIME)


# Turn date string into datetime object
def date_obj(date: str) -> dt:
    return dt.datetime.strptime(date, DATE_HUMAN_TIME)


def date_dif_today(date: dt.datetime) -> dt.timedelta:
    delta: dt.timedelta = date_obj(date_norm()) - date
    print(delta)
    print(delta.days)
    print(delta.seconds)
    print(delta.microseconds)
    return delta

