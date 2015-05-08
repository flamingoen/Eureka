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

    KB.append(Clause([Litteral("b"), Litteral("d", False)]))

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
    tempKB=[]
    for temp in foundClauses:
        tempKB.append(temp.reduced(node))
    counter = -1
    for clause in foundClauses:
        counter = counter + 1
        new = tempKB[counter]
        if new == node:
            continue
        for i in range(len(tempKB)):
            if i!=counter:
                new.KB.append(tempKB[i])
        #Adds the difference between the lists.
        for clause1 in node.KB:
            addClause=True
            for clause2 in foundClauses:
                if clause1 == clause2 or clause1 in new.KB:
                    addClause = False
            if addClause:
                new.KB.append(clause1)
        print new

        if not new.KB:
            print "true"
            return True
        if new.KB == node.KB:
            print"false"
            return False

        forwardChaining(new)

# sets up base case
createKB()
start = Clause([contradiction])
start.KB = KB

print forwardChaining(start)

#swag