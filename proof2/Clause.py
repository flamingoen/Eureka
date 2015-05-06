class Clause:

    def __init__(self,litterals):
        self.litterals = litterals
        self.KB = []
        self.neighbours = []

    def __eq__(self, other):
        return (self.litterals == other.litterals)

    def contains(self, litteral):
        for internLitteral in self.litterals:
            if internLitteral.char == litteral.char:
                return True
        return False

    def reduced(self, clause):
        litterals = []
        for internLitteral in self.litterals:
            for clauseLiteral in clause.litterals:
                if not internLitteral.opposite(clauseLiteral):
                    litterals.append(internLitteral)

        filter(None, litterals)
        return Clause(litterals)

    def __str__(self):
        str = ""
        for litteral in self.litterals:
            str = str + " " + litteral.__str__()
        return str