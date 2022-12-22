from colorama import Fore

MAX_WIDTH: int = 80


class Fmt:
    BLD: str = '\033[1m'
    ITL: str = '\033[3m'
    UND: str = '\033[4m'
    END: str = '\033[0m'


def bld(text: str) -> str:
    return Fmt.BLD + text + Fmt.END


def itl(text: str) -> str:
    return Fmt.ITL + text + Fmt.END


def und(text: str) -> str:
    return Fmt.UND + text + Fmt.END


def msg(text: str) -> str:
    return bld(Fore.CYAN + text)


def imp(text: str) -> str:
    return Fore.RED + bld(text)


def warn(text: str) -> str:
    return itl(Fore.YELLOW + text)


def suc(text: str) -> str:
    return Fore.LIGHTGREEN_EX + text + Fmt.END


# Formats passed text as a header
def heading(text: str) -> str:
    return grn_b(text)


# Formats passed text as code
def code(text: str) -> str:
    return bld(text)


def line(char=None, length=None) -> str:
    if not char:
        char: str = '-'
    if not length:
        length: int = MAX_WIDTH

    return Fore.LIGHTBLACK_EX + char * length + Fore.RESET


def lred_b(text: str) -> str:
    return Fore.LIGHTRED_EX + bld(text) + Fore.RESET


def grn_b(text: str) -> str:
    return Fore.GREEN + bld(text) + Fore.RESET


def yel_b(text: str) -> str:
    return Fore.YELLOW + bld(text) + Fore.RESET


def lcyan(text: str) -> str:
    return Fore.LIGHTCYAN_EX + text + Fore.RESET


def lyel(text: str) -> str:
    return Fore.LIGHTYELLOW_EX + text + Fore.RESET


def gray(text: str) -> str:
    return Fore.LIGHTBLACK_EX + text + Fore.RESET


