from ut import warn


class InvalidInput(Exception):
    def __init__(self, place, inp):
        self.place = place
        self.inp = inp

    def __str__(self):
        return warn(f"Input for '{self.place}' not recognized: {self.inp}")


class ListingItemNotExist(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Number provided does not correspond to an item: {self.err}")


class OutsidePageBounds(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Already on {self.err} page.")


class NoPagesInListing(Exception):
    def __str__(self):
        return warn("Empty listing!")


class MissingArguments(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"'{self.err}' must take arguments.")


class MissingSearchQuery(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"'{self.err}' must take a search query.")


class MatchNotFound(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"No matches found for '{self.err}'")


class SelectBeforeModify(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Select a note to {self.err}")


class NoSuchCommand(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"No such command for qnot: {self.err}")


class NotListable(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return warn(f"Nothing to list for: {self.err}")


class ListBeforeSelect(Exception):
    def __str__(self):
        return warn(f"Find notes to select.")
