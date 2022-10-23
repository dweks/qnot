class Fmt:
    BLD = '\033[1m'
    ITL = '\033[3m'
    UND = '\033[4m'
    END = '\033[0m'


def bld(string):
    return Fmt.BLD + string + Fmt.END


def itl(string):
    return Fmt.ITL + string + Fmt.END


def und(string):
    return Fmt.UND + string + Fmt.END


def heading(text):
    return und(text)


def code(text, preline=False, postline=False):
    newstr = bld(text)
    if preline:
        newstr = "\n" + newstr
    if postline:
        newstr += "\n"
    return newstr
