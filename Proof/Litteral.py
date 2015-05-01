class Litteral:

    def __init__(self, bol=True, char=None):
        self.char = char
        self.bol = bol

    def __eq__(self, other):
        return (self.bol == other.bol) and (self.char == other.char)

    def Not(self):
        self.bol = not self.bol