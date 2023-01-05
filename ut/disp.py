from colorama import Fore

MAX_WIDTH: int = 80
DO_FMT: bool = True


class Dec:
    BLD: str = '\033[1m'
    ITL: str = '\033[3m'
    UND: str = '\033[4m'
    END: str = '\033[0m'


def f(text: str, c: str = None, s: str = None, dofmt: bool = DO_FMT) -> str:
    if not dofmt:
        return text
    color = {
        None: text,
        "r": Fore.RED + text + Fore.RESET,
        "lr": Fore.LIGHTRED_EX + text + Fore.RESET,
        "y": Fore.YELLOW + text + Fore.RESET,
        "ly": Fore.LIGHTYELLOW_EX + text + Fore.RESET,
        "g": Fore.GREEN + text + Fore.RESET,
        "lg": Fore.LIGHTGREEN_EX + text + Fore.RESET,
        "b": Fore.BLUE + text + Fore.RESET,
        "lb": Fore.LIGHTBLUE_EX + text + Fore.RESET,
        "m": Fore.MAGENTA + text + Fore.RESET,
        "lm": Fore.MAGENTA + text + Fore.RESET,
        "c": Fore.CYAN + text + Fore.RESET,
        "lc": Fore.LIGHTCYAN_EX + text + Fore.RESET,
        "blk": Fore.BLACK + text + Fore.RESET,
        "gry": Fore.LIGHTBLACK_EX + text + Fore.RESET,
        "w": Fore.WHITE + text + Fore.RESET,
        "lw": Fore.LIGHTWHITE_EX + text + Fore.RESET,
    }
    text = color[c]

    if s:
        if 'b' in s:
            text = Dec.BLD + text + Dec.END
        if 'u' in s:
            text = Dec.UND + text + Dec.END
        if 'i' in s:
            text = Dec.ITL + text + Dec.END

    return text


def bld(text: str) -> str:
    return Dec.BLD + text + Dec.END


def itl(text: str) -> str:
    return Dec.ITL + text + Dec.END


def und(text: str) -> str:
    return Dec.UND + text + Dec.END


def msg(text: str) -> str:
    return lblu_b(text)


def imp(text: str) -> str:
    return f(text, 'r')


def warn(text: str) -> str:
    return f(text, 'ly', 'i')


def suc(text: str) -> str:
    return f(text, 'g')


# Formats passed text as a header
def heading(text: str) -> str:
    return f(text, 'g', 'bi')


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


def lgrn_b(text: str) -> str:
    return Fore.LIGHTGREEN_EX + bld(text) + Fore.RESET


def yel_b(text: str) -> str:
    return Fore.YELLOW + bld(text) + Fore.RESET


def lcyan_b(text: str) -> str:
    return Fore.LIGHTCYAN_EX + bld(text) + Fore.RESET


def cyan(text: str) -> str:
    return Fore.CYAN + text + Fore.RESET


def lblu_b(text: str) -> str:
    return Fore.LIGHTBLUE_EX + bld(text) + Fore.RESET


def lyel(text: str) -> str:
    return Fore.LIGHTYELLOW_EX + text + Fore.RESET


def gry(text: str) -> str:
    return Fore.LIGHTBLACK_EX + text + Fore.RESET
