from Litteral import *
from Clause import *

KB = []
contradiction = Litteral("a", False)

# Knowledgebase
def createKB():

    KB.append(Clause([Litteral("a"), Litteral("b", False)]))

    KB.append(Clause([Litteral("a"), Litteral("c", False)]))

    KB.append(Clause([Litteral("b"), Litteral("b", False)]))

    KB.append(Clause([Litteral("b"), Litteral("c", False)]))

    KB.append(Clause([Litteral("b"), Litteral("c", False)]))

    KB.append(Clause([Litteral("c")]))

    KB.append(Clause([Litteral("d")]))


def forwardChaining(node):
    foundClauses = []

    # finding clause matching node
    for clause in node.KB:
        for litteral in node.litterals:
            if clause.contains(litteral):
                foundClauses.append(clause)

    # make new node, check if branch is done or continue
    for clause in foundClauses:
        new = clause.reduced(node)
        new.KB = [clause for clause in node.KB if clause not in foundClauses] # laver en ny kb af start.KB hvor de fundet clauses i newClauses er fjernet - virker ikke da to clauses godt kan være ens med med forskellig id

        print new

        if not new.KB:
            return True
        if new.KB == node.KB:
            return False

        forwardChaining(new)

# sets up base case
createKB()
start = Clause([contradiction])
start.KB = KB

print forwardChaining(start)
