class Litteral:

    def __init__(self, char=None, bol=True, reduced=False):
        self.char = char
        self.bol = bol
        self.reduced = reduced

    def __eq__(self, other):
        return (self.bol == other.bol) and (self.char == other.char)

    def __ne__(self, other):
        return (self.bol != other.bol) and (self.char != other.char)

    def Not(self):
        self.bol = not self.bol

    def opposite(self, litteral):
        if (litteral.char == self.char) and (self.bol != litteral.bol):
            return True
        return False

    def __str__(self):
        if self.char == "":
            return ""
        if self.bol:
            return self.char
        return "NOT "+self.char
