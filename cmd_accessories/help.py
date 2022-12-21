from ut.disp import heading, itl, und, code, bld


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

{code("  qnot <cmd_accessories> <args>")}

Commands can be expanded or not ({code("-full")} or {code("-f")}).
Some commands take arguments; if none supplied, {und("interface mode")} starts.

To list all available commands: {bld("  qnot -h list")}
To get details on a specific cmd_accessories: {bld("  qnot -h " + itl("<cmd_accessories>"))}

{heading("INTERFACE MODE")}

If needed, qnot will execute a program with a menu with prompt.
This occurs if no arguments are given for a cmd_accessories that needs them.
When interface mode starts, exit without changing by entering {bld("q")} anytime.
"""

