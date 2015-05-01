class Litteral:

    def __init__(self, char=None, bol=True):
        self.char = char
        self.bol = bol

    def __eq__(self, other):
        return (self.bol == other.bol) and (self.char == other.char)

    def Not(self):
        self.bol = not self.bol

    def __str__(self):
        if self.bol:
            return self.char
        return "NOT "+self.char
