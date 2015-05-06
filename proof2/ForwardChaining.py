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

createKB()

pool = []

start = Clause([contradiction])
start.KB = KB


foundClauses = []
for clause in start.KB:
    for litteral in start.litterals:
        if clause.contains(litteral):
            foundClauses.append(clause)

for clause in foundClauses:
    new = clause.reduced(start)
    new.KB = [x for x in start.KB if x not in foundClauses]
    pool.append(new)

for p in pool:
    print p
