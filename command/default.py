from output import Output

# If an Admin object is created without parameters, this is the default
# 'dispatched' command.
def exec_default(args=None):
    return Output(['this', 'is', 'default', 'for', 'admin'])
