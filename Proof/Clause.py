class Clause:

    def __init__(self,litterals):
        self.litterals = litterals
        self.KB = []
        self.neighbours = []

    def __eq__(self, other):
        return (self.litterals == other.litterals)