
class Path:
    def __init__(self, top, mid, fname):
        self.__top = top
        self.__mid = mid
        self.__fname = fname

    def get_full_path(self):
        if self.__mid is None:
            return '/'.join((self.__top, self.__fname))
        return '/'.join((self.__top, self.__mid, self.__fname))

    def get_top(self):
        return self.__top

    def get_mid(self):
        return self.__mid

    def get_fname(self):
        return self.__fname

    def get_top_mid(self):
        return '/'.join((self.__top, self.__mid))

    def get_mid_fname(self):
        return '/'.join((self.__mid, self.__fname))

    def set_fname(self, fname):
        self.__fname = fname
