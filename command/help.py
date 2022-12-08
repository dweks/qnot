from util import bld, itl, und, heading, code


# Entry-point for command called from dispatch table in Admin or Standard
# Help uses a dispatch table for the help 'topics'. The command's parameterless
# behavior is to TODO display a list of available help topics
def exec_help(args):
    message_table = {
        None: BASIC,
        'view': VIEW,
        'edit': EDIT,
        'full': FULL,
        'tag': TAG,
        'title': TITLE,
        'remove': REMOVE,
    }

    arg = None if not args else args[0]
    if arg not in message_table.keys():
        print(f"Invalid argument for 'help': \"{arg}\"")
    else:
        return message_table[arg]


VIEW = "h_view"
EDIT = "h_edit"
FULL = "h_full"
TAG = "h_tag"
TITLE = "h_title"
REMOVE = "h_remove"
BASIC = f"""
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
"""
