from util import prb


class InvalidInput(Exception):
    def __init__(self, place, inp):
        self.place = place
        self.inp = inp

    def __str__(self):
        return prb(f"Input for '{self.place}' not recognized: {self.inp}")


class ListingItemNotExist(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return prb(f"Index provided does not correspond to an item: {self.err}")


class OutsidePageBounds(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return prb(f"Exceeded page bounds; total pages: {self.err}")


class NoPagesInListing(Exception):
    def __str__(self):
        return prb("Empty listing!")


class MissingArguments(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return prb(f"'{self.err}' must take arguments")


class MissingSearchQuery(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return prb(f"'{self.err}' must take a search query")


class MatchNotFound(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return prb(f"No matches found for '{self.err}'")


class SelectBeforeModify(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return prb(f"Select a note to {self.err}")


class NotListable(Exception):
    def __init__(self, err):
        self.err = err

    def __str__(self):
        return prb(f"Nothing to list for: {self.err}")
