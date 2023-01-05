from ut.disp import warn


class QnotException(Exception):
    def __init__(self):
        pass


class InvalidInput(QnotException):
    def __init__(self, place, inp):
        self.source = place
        self.inp = inp

    def __str__(self):
        return warn(f"`{self.inp}` not recognized.")


class ListingItemNotExist(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Number provided does not correspond to an item: {self.err}")


class OutsidePageBounds(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Already on {self.err} page.")


class NoPagesInListing(QnotException):
    def __str__(self):
        return warn("Empty listing!")


class MissingArguments(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"'{self.err}' must take arguments.")


class MissingSearchQuery(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"{self.err} must take a search query.")


class MatchNotFound(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"No matches found for: {self.err}")


class SelectBeforeModify(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Not in selection mode, first select note to use this command.")


class NoSuchCommand(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"No such command for qnot: {self.err}")


class NotListable(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Nothing to list for {self.err}; Enter `list list` to see listable keywords.")


class ListBeforeSelect(QnotException):
    def __str__(self):
        return warn(f"Find notes to select.")


class FileNotExist(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"File does not exist: {self.err}")


class EmptyDirectory(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Provided directory has no importable files: {self.err}")


class InvalidSelection(QnotException):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Invalid selection: {self.err}")
