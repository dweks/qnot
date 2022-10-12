from parse import parse_command


class Help:
    @staticmethod
    def basic_instructions():
        print("Basic Usage:")
        print()
        print("(1) Create new note (with title):")
        print("    qnot some title :: note with +tags")
        print()
        print("(2) Create new note (without title):")
        print("    qnot note with +tags")
        print()
        print("(3) View note (interface)")
        print("    qnot view")
        print()
        print("(4) View note (with arguments)")
        print("    qnot view <argument>")
        print()
        print("(5) Detailed help")
        print("    qnot help <argument>")
        print("    NOTE: Replace <argument> with command:")
        print("       view, help, edit, remove, tags")


def handle_command(argv):
    cmd = parse_command(argv)

