from db_access import select_last_note
from exceptions import MatchNotFound, InvalidInput
from listing import Listing
from ut import add_tags_to_note


def exec_last(args=None):
    if args:
        if not args[0].isdigit() or int(args[0]) == 0:
            raise InvalidInput("last", args[0])
        num = int(args[0])
    else:
        num = 1
    result = select_last_note(num)
    if not result or len(result) == 0:
        raise MatchNotFound(f"last {num} created")
    return Listing(f"Last {num} created", add_tags_to_note(result))
