from display import bld, itl, und, heading, code


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
    itl("[ " + und("COMMAND: view") + " ]"),
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
    print(f"""
{heading("QNOT")}: Create, view, edit, or delete notes with simple commands.

{heading("NOTE SYNTAX")}

{bld("Title: ")} Anything before the first :: will be considered a title.
{bld("Tags: ")} Include tags by prefixing any word with a +, anywhere in your entry.

{heading("WRITING QNOTES")}

{code("  qnot here is my note")}
{code("  qnot with a title :: here is my note")}
{code("  qnot here is my note +with +tags")}
{code('  qnot "here is my note with $pec!^| (har*<ters "')}

{heading("WRITING EXTENDED NOTES")}

Extended notes will open a default text-editor for note-taking with more formatting.

{code("  qnot -f")}

Note will be saved as qnot if editor successfully writes.
Extended notes preserve whitespace and allow special characters.

{heading("COMMANDS")}

{code("  qnot <command> <args>")}

Commands can be expanded or not ({code("-full")} or {code("-f")}).
Some commands take arguments; if none supplied, {und("interface mode")} starts.

To list all available commands: {bld("  qnot -h list")}
To get details on a specific command: {bld("  qnot -h " + itl("<command>"))}

{heading("INTERFACE MODE")}

If needed, qnot will execute a program with a menu with prompt.
This occurs if no arguments are given for a command that needs them.
When interface mode starts, exit without changing by entering {bld("q")} anytime.
    """)
