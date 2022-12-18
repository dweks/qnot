from db_access import select_like
from exceptions import MatchNotFound
from ut import debug, add_tags_to_note
from listing import Listing


def exec_search(query):
    result = select_like(query)
    if result is None or len(result) == 0:
        raise MatchNotFound(f"{' '.join(query)}")
    return Listing(f"Searching for ` {' '.join(query)} `", add_tags_to_note(result))
