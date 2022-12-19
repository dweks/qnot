from db_access import select_like
from exceptions import MatchNotFound, MissingSearchQuery
from listing import Listing
from ut import add_tags_to_note


def exec_search(query):
    if not query:
        raise MissingSearchQuery("search")
    result = select_like(query)
    if result is None or len(result) == 0:
        raise MatchNotFound(f"{' '.join(query)}")
    return Listing(f"Searching for ` {' '.join(query)} `", add_tags_to_note(result))
