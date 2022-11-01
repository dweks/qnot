# Contains all output that commands produce.

class Output:
    def __init__(self, listing):
        self.listing = listing

    def display(self):
        print(self.listing)
