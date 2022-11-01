from command import *


class Standard:
    dispatch = {
        'quick': exec_quick,
        'full': exec_full,
    }

    def __init__(self, cmd=None, args=None):
        self.execute(cmd, args)

    def execute(self, cmd, args):
        if cmd in self.dispatch.keys():
            return self.dispatch[cmd](args)

        raise ValueError(f"Invalid command: '{cmd}'")
