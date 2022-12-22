from ut.disp import Fore


def debug(var: any):
    print(Fore.LIGHTMAGENTA_EX + str(var) + Fore.RESET)


def ldebug(title: str, var: any):
    print(Fore.LIGHTMAGENTA_EX + f"{title}: " + str(var) + Fore.RESET)


def typeval(var: any, title: str = None):
    if title is not None:
        print(Fore.LIGHTMAGENTA_EX + f"_{title}_: [TYPE]:", type(var), "[VAL]:", str(var) + Fore.RESET)
    else:
        print(Fore.LIGHTMAGENTA_EX + "[TYPE]:", type(var), "[VAL]:", str(var) + Fore.RESET)
