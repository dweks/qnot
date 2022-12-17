from db_access import select_last_note, select_notetags
from exceptions import MatchNotFound, InvalidInput
from listing import Listing
from util import debug


def exec_last(args=None):
    if args is not None:
        if not args[0].isdigit() or int(args[0]) == 0:
            raise InvalidInput("last", args[0])
        num = int(args[0])
    else:
        num = 1
    res = select_last_note(num)
    if res is None or len(res) == 0:
        raise MatchNotFound(f"last {num} created")

    new_res = []
    for note in res:
        if note is None:
            break
        new_tags = None
        raw_tags = select_notetags(note[0])
        if raw_tags is not None:
            new_tags = [tag for tup in raw_tags for tag in tup]
        note += (new_tags,)
        new_res.append(note)

    return Listing(f"Last {num} created", new_res)
