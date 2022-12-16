from db_access import select_last
from exceptions import MatchNotFound, InvalidInput
from listing import Listing


def exec_last(args=None):
    if args is not None:
        if not args[0].isdigit() or int(args[0]) == 0:
            raise InvalidInput("last", args[0])
        num = int(args[0])
    else:
        num = 1

    res = select_last(num)
    if res is None or len(res) == 0:
        raise MatchNotFound("last added")
    return Listing(f"Last {num} created", res)
