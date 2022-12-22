from dispatch.adm import admin_dispatch
from dispatch.mod import mod_dispatch
from dispatch.std import std_dispatch


class Carg:
    def __init__(self, cmd: str or None, args: list or None):
        self.c: str = cmd
        self.a: list = args

    def is_none(self) -> bool:
        return self.c is None and self.a is None

    def has_args(self) -> bool:
        return self.a is not None

    def is_sel(self) -> bool:
        return not self.is_none() and self.c[0].isdigit()

    def is_adm(self) -> bool:
        return self.c in admin_dispatch.keys()

    def is_mod(self) -> bool:
        return self.c in mod_dispatch.keys()

    def is_std(self) -> bool:
        return self.c in std_dispatch.keys()

    def num_args(self) -> int:
        return len(self.a) if self.a else 0

    def type_args(self) -> type:
        return type(self.a)

    def arg_str(self) -> str:
        if self.a is not None:
            return ' '.join(self.a)
        return "None"

    def cmd_str(self) -> str:
        if self.c is not None:
            return str(self.c)
        return "None"

    def __str__(self):
        return self.cmd_str() + ' ' + self.arg_str()


