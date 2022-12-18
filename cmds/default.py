from .find import exec_get


# If an Admin object is created without parameters, this is the default
# 'dispatched' cmds.
def exec_default(args=None):
    exec_get(["one"])
