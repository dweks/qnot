from ut import bld, itl, und, heading, code
from exceptions import InvalidInput


# Entry-point for cmds called from dispatch table in Admin or Standard
# Help uses a dispatch table for the help 'topics'. The cmds's parameterless
# behavior is to TODO display a list of available help topics
def exec_help(args):
    # todo set default help message for empty args
    arg = None if not args else args[0]
    if arg not in help_dispatch.keys():
        raise InvalidInput("help", arg)
    else:
        print(help_dispatch[arg])
    return "suspend"


VIEW = "h_view"
EDIT = "h_edit"
FULL = "h_full"
TAG = "h_tag"
TITLE = "h_title"
REMOVE = "h_remove"
FIND = f"""{heading(f"How to use the 'get' command:")}
{itl("Purpose")}: Retrieves notes by tag
{itl("Context")}: Linux and qnot admin mode
{itl("Arguments")}: One or more tags with optional filter 
{itl("Filters")}: Only retrieve notes created in time range: today, week, day

{und("Basic Usage")}: 
  Linux:\n{code("    qnot -get [filter] <tag>")}
  Admin:\n{code("    get [filter] <tag>")}
"""
ADD = "h_add"
LIST = "h_list"
NEXT = "h_next"
PREV = "h_prev"
LAST = "h_last"
TODAY = "h_today"
WEEK = "h_week"
DAY = "h_day"
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

{code("  qnot <cmds> <args>")}

Commands can be expanded or not ({code("-full")} or {code("-f")}).
Some commands take arguments; if none supplied, {und("interface mode")} starts.

To list all available commands: {bld("  qnot -h list")}
To get details on a specific cmds: {bld("  qnot -h " + itl("<cmds>"))}

{heading("INTERFACE MODE")}

If needed, qnot will execute a program with a menu with prompt.
This occurs if no arguments are given for a cmds that needs them.
When interface mode starts, exit without changing by entering {bld("q")} anytime.
"""

help_dispatch = {
    'v': VIEW,
    'view': VIEW,
    'e': EDIT,
    'edit': EDIT,
    'full': FULL,
    'r': REMOVE,
    'remove': REMOVE,
    'g': FIND,
    'get': FIND,
    'a': ADD,
    'add': ADD,
    'ls': LIST,
    'list': LIST,

    'n': NEXT,
    'next': NEXT,
    'p': PREV,
    'prev': PREV,
    'l': LAST,
    'last': LAST,

    'tag': TAG,
    'title': TITLE,
    'today': TODAY,
    'week': WEEK,
    'day': DAY,
}
