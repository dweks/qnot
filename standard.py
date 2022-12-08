from dispatch import standard_dispatch as dispatch


class Standard:
    def __init__(self, cmd=None, args=None):
        self.execute(cmd, args)

    def execute(self, cmd, args):
        if cmd in dispatch.keys():
            return dispatch[cmd](args)

        raise ValueError(f"Invalid command: '{cmd}'")
