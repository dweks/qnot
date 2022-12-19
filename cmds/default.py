from .last import exec_last


# If an Admin object is created without parameters, this is the default
# 'dispatched' cmds.
def exec_default(args=None):
    return exec_last(5)
