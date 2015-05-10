class Clause:

    def __init__(self,litterals):
        self.litterals = litterals
        self.KB = []
        self.neighbours = []

    def __eq__(self, other):
        if other == "":
            return len(self.litterals) == 0
        return (self.litterals == other.litterals)

    def __ne__(self, other):
        if other == "":
            return len(self.litterals) != 0
        return (self.litterals != other.litterals)

    def contains(self, litteral):
        for internLitteral in self.litterals:
            if internLitteral.char == litteral.char:
                return True
        return False

    def reduced(self, clause):
        litterals = []
        for internLitteral in self.litterals:
            for clauseLitteral in clause.litterals:
                if not internLitteral.opposite(clauseLitteral):
                    if  internLitteral not in litterals:
#                        clauseLitteral.reduced = True
                        litterals.append(internLitteral)
                else:
                    clauseLitteral.reduced = True
        filter(None, litterals)
        return Clause(litterals)

    def __str__(self):
        str = ""
        for litteral in self.litterals:
            str = str + " " + litteral.__str__()
        return str