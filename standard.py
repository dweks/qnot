from dispatch import std_dispatch


class Standard:
    def __init__(self, carg):
        std_dispatch[carg.c](carg.a)
