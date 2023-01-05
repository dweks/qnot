import cmd_accessories.help as hlp
help_dispatch = {
    'basic': hlp.BASIC,
    'e': hlp.EDIT,
    'edit': hlp.EDIT,
    'ex': hlp.FULL,
    'del': hlp.DELETE,
    'delete': hlp.DELETE,
    'g': hlp.GET,
    'get': hlp.GET,
    'a': hlp.ADD,
    'add': hlp.ADD,
    'ls': hlp.LIST,
    'list': hlp.LIST,

    'n': hlp.NEXT,
    'next': hlp.NEXT,
    'p': hlp.PREV,
    'prev': hlp.PREV,
    'l': hlp.LAST,
    'last': hlp.LAST,

    'tag': hlp.TAG,
    'title': hlp.TITLE,
    'today': hlp.TODAY,
    'week': hlp.WEEK,
    'day': hlp.DAY,
}
