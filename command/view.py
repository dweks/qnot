# TODO put together some dummy notes to test with

# Entry-point for command called from dispatch table in Admin

def exec_view(args):
    pass


def lister(found_notes):
    # TODO have a maximum display with a "view more?" option
    len_cap = 40
    count = 1
    for entry in found_notes:
        title = entry["title"]
        note = entry["note"]
        tags = entry["tags"]

        print(f"({count}) ", note if len(note) <= len_cap else entry[:40])
        count += 1
