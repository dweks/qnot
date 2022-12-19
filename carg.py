import dispatch as dsp


class Carg:
    def __init__(self, cmd, args):
        self.c = cmd
        self.a = args

    def is_none(self):
        return self.c is None and self.a is None

    def has_args(self):
        return self.a is not None

    def is_sel(self):
        return not self.is_none() and self.c[0].isdigit()

    def is_adm(self):
        return self.c in dsp.admin_dispatch.keys()

    def is_mod(self):
        return self.c in dsp.mod_dispatch.keys()

    def is_std(self):
        return self.c in dsp.std_dispatch.keys()

    def num_args(self):
        return len(self.a) if self.a else 0

    def type_args(self):
        return type(self.a)

    def arg_str(self):
        if self.a:
            return str(arg for arg in self.a)
        return "None"

    def cmd_str(self):
        if self.c:
            return str(self.c)
        return "None"

    def __str__(self):
        return self.cmd_str() + ' ' + self.arg_str()
