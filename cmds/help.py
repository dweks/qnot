from util import bld, itl, und


def exec_help(args):
    message = {
        "view": help_view,
        "edit": help_edit,
        "full": help_full,
        "tag": help_tag,
        "title": help_title,
        "remove": help_remove,
        "list": help_list,
        None: help_basic
    }

    arg = None if not args else args[0]
    if arg not in message.keys():
        print(f"Invalid argument for 'help': \"{arg}\"")
    else:
        message[arg]()


def help_view():
    itl("\n[ " + und("COMMAND: view") + " ]\n"),
    pass


def help_edit():
    print("help edit")
    pass


def help_full():
    print("help full")
    pass


def help_tag():
    print("help tag")
    pass


def help_title():
    print("help title")
    pass


def help_remove():
    print("help remove")
    pass


def help_list():
    print("help list")
    pass


def help_basic():
    print(
        itl("\n[ " + und("QNOT BASICS") + " ]\n"),
        "Create, view, edit, or delete notes with simple commands.\n",

        itl("\n[ " + und("NOTE SYNTAX") + " ]\n"),
        "Anything before the first :: will be considered a title.",
        "Include tags by prefixing any word with a +, anywhere in your entry.",

        itl("\n[ " + und("WRITING QNOTES") + " ]\n"),
        bld("  qnot here is my note"),
        bld("  qnot with a title :: here is my note"),
        bld("  qnot here is my note +with +tags"),
        bld(r'  qnot "here is my note with $pec!^|   \t   (har*<ters "'),

        itl("\n[ " + und("WRITING EXTENDED NOTES") + " ]\n"),
        bld("  qnot -f"),
        "\nNote will be saved as qnot if editor successfully writes.",
        "Extended notes preserve whitespace and allow special characters.",

        itl("\n[ " + und("COMMANDS") + " ]\n"),
        bld("  qnot <command> <args>"),
        "\nCommands can be expanded or not (" + bld("-full") + " or " + bld("-f") + ").",
        "Some commands take arguments; if none supplied, " + und("interface mode") + " starts.",

        "\nTo list all available commands:\n",
        bld("  qnot -h list"),
        "\nTo get details on a specific command: \n",
        bld("  qnot -h " + itl("<command>")),

        itl("\n[ " + und("INTERFACE MODE") + " ]\n"),
        "If needed, qnot will execute a program with a menu with prompt. ",
        "This occurs if no arguments are given for a command that needs them.",
        "When interface mode starts, exit without changing by entering " + bld("q") + " anytime.",
        sep='\n'
    )
