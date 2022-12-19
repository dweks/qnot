from colorama import Fore
MAX_WIDTH = 80
# Output text formatting


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
    return grn_b(string)


# Formats passed string as code
def code(string):
    return bld(string)


def line(char=None, length=None):
    if not char:
        char = '-'
    if not length:
        length = MAX_WIDTH

    return Fore.LIGHTBLACK_EX + char * length + Fore.RESET


def lred_b(string):
    return Fore.LIGHTRED_EX + bld(string) + Fore.RESET


def grn_b(string):
    return Fore.GREEN + bld(string) + Fore.RESET


def yel_b(string):
    return Fore.YELLOW + bld(string) + Fore.RESET


def lcyan(string):
    return Fore.LIGHTCYAN_EX + string + Fore.RESET


def lyel(string):
    return Fore.LIGHTYELLOW_EX + string + Fore.RESET


def gray(string):
    return Fore.LIGHTBLACK_EX + string + Fore.RESET


def debug(string):
    print(Fore.LIGHTMAGENTA_EX + str(string) + Fore.RESET)
