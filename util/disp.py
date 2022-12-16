from colorama import Fore
# Output text formatting


# Escape sequences for bold, italics, underline
class Fmt:
    BLD = '\033[1m'
    ITL = '\033[3m'
    UND = '\033[4m'
    END = '\033[0m'


# Formats passed string with bold
def bld(string):
    return Fmt.BLD + string + Fmt.END


# Formats passed string with italics
def itl(string):
    return Fmt.ITL + string + Fmt.END


# Formats passed string with underline
def und(string):
    return Fmt.UND + string + Fmt.END


# Qnot communication messages

def msg(string):
    return bld(Fore.CYAN + string)


def imp(string):
    return itl(Fore.RED + bld(string))


def prb(string):
    return itl(Fore.YELLOW + string)


# Formats passed string as a header
def heading(string):
    return und(string)


# Formats passed string as code
def code(string):
    return bld(string)
