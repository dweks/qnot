from dispatch import admin_dispatch, mod_dispatch, std_dispatch


class Carg:
    def __init__(self, cmd=None, args=None):
        self.c: str = cmd
        self.a: list = args if args is not None else []

    def is_sel(self) -> bool:
        return not self.is_empty() and self.c[0].isdigit() or self.c == "all"

    def is_adm(self) -> bool:
        return self.c in admin_dispatch.keys()

    def is_mod(self) -> bool:
        return self.c in mod_dispatch.keys()

    def is_std(self) -> bool:
        return self.c in std_dispatch.keys()

    def is_empty(self) -> bool:
        return self.c is None

    def has_args(self) -> bool:
        return len(self.a) > 0

    def num_args(self) -> int:
        return len(self.a)

    def type_args(self) -> type:
        return type(self.a)

    def arg_str(self) -> str:
        if self.num_args() > 0:
            return ' '.join(self.a)
        return "NOARGS"

    def cmd_str(self) -> str:
        if len(self.c) > 0:
            return str(self.c)
        return "NOCMD"

    def __str__(self):
        return self.cmd_str() + ' ' + self.arg_str()
