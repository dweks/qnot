from colorama import Fore
MAX_WIDTH = 80
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
    return Fore.RED + bld(string)


def warn(string):
    return itl(Fore.YELLOW + string)


def suc(string):
    return Fore.LIGHTGREEN_EX + string + Fmt.END


# Formats passed string as a header
def heading(string):
    return und(string)


# Formats passed string as code
def code(string):
    return bld(string)


def line(char=None, length=None):
    if not char:
        char = '-'
    if not length:
        length = MAX_WIDTH

    return Fore.LIGHTBLACK_EX + char * length + Fmt.END


def lred_b(string):
    return Fore.LIGHTRED_EX + bld(string) + Fmt.END


def cyan_b(string):
    return Fore.LIGHTCYAN_EX + string + Fmt.END


def lyel(string):
    return Fore.LIGHTYELLOW_EX + string + Fmt.END


def gray(string):
    return Fore.LIGHTBLACK_EX + string + Fmt.END


def debug(string):
    print(Fore.LIGHTMAGENTA_EX + str(string) + Fmt.END)
