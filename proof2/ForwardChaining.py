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

    KB.append(Clause([Litteral("d")]))

    KB.append(Clause([Litteral("d")]))


def forwardChaining(node):
    foundClauses = []
    # finding clause matching node
    for clause in node.KB:
        for litteral in node.litterals:
            if clause.contains(litteral):
                foundClauses.append(clause)

    # make new node, check if branch is done or continue
    reducedFoundClauses=[]
    for temp in foundClauses:
        reducedNode = temp.reduced(node)
        if  reducedNode != node:
            reducedFoundClauses.append(reducedNode)
    counter = -1
    for clause in reducedFoundClauses:
        counter = counter + 1
        new = reducedFoundClauses[counter]
        if new == node:
            continue
        #removes any litterals that have been used for reduction---------------------------------------------------
     #   unchanged = True
        for litteral in node.litterals:
            if litteral.reduced:
                node.litterals.remove(litteral)
     #           unchanged = False
     #   if node!= "":
     #       new.KB.append(node)
     #   if unchanged:
     #       continue
        #----------------------------------------------------------------------------------------------------------
        for i in range(len(reducedFoundClauses)):
            if i!=counter:
                new.KB.append(reducedFoundClauses[i])
        #Adds the difference between the lists.
        for clause1 in node.KB:
            addClause=True
            for clause2 in foundClauses:
                if clause1 == clause2 or clause1 in new.KB:
                    addClause = False
            if addClause:
                new.KB.append(clause1)
        if new == "":
            if len(new.KB) == 0:
                return True
            new.litterals = new.KB.pop(0).litterals

        print new

        #if not new.KB:
        #    print "true"
        #    return True
       # if new.KB == node.KB:
       #     print"false"
       #     return False

        if forwardChaining(new):
            return True
    return False
# sets up base case
createKB()
start = Clause([contradiction])
start.KB = KB

print forwardChaining(start)