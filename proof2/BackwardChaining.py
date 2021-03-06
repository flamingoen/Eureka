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

    KB.append(Clause([Litteral("a")]))


def createKB2():
    #Actural KB
    KB.append(Clause([Litteral("w"), Litteral("ok-pump", False)]))
    KB.append(Clause([Litteral("w"), Litteral("on-pump", False)]))
    KB.append(Clause([Litteral("w"), Litteral("man-fill", False)]))
    KB.append(Clause([Litteral("man-fill"), Litteral("on-pump")]))
    KB.append(Clause([Litteral("man-fill"), Litteral("on-pump")]))
    KB.append(Clause([Litteral("w", False), Litteral("steam")]))
    KB.append(Clause([Litteral("ok-boiler", False), Litteral("steam")]))
    KB.append(Clause([Litteral("on-boiler", False), Litteral("steam")]))
    KB.append(Clause([Litteral("steam", False), Litteral("w", False)]))
    KB.append(Clause([Litteral("w", False), Litteral("steam")]))
    KB.append(Clause([Litteral("on-boiler"), Litteral("steam", False)]))
    KB.append(Clause([Litteral("ok-boiler"), Litteral("steam", False)]))
    KB.append(Clause([Litteral("steam", False), Litteral("hot-drink")]))
    KB.append(Clause([Litteral("coffee", False), Litteral("hot-drink")]))
    KB.append(Clause([Litteral("steam", False), Litteral("hot-drink")]))
    KB.append(Clause([Litteral("tea", False), Litteral("hot-drink")]))
    KB.append(Clause([Litteral("coffee"), Litteral("tea")]))

    #contradiction
    KB.append(Clause([Litteral("ok-pump"), Litteral("hot-drink", False)]))
    KB.append(Clause([Litteral("on-pump"), Litteral("hot-drink", False)]))

def backwardChaining(node,current_goals):
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
        if  reducedNode != node and reducedNode != "":
            reducedFoundClauses.append(reducedNode)
     #-----------------------------------------------------------------------------------
    for clause in reducedFoundClauses:
        isNewGoal = True
        for goal in current_goals:
            if clause == goal:
                isNewGoal = False
        if isNewGoal:
            current_goals.append(clause)
#------------------------------------------------------------------------------------

    counter = -1
    for clause in reducedFoundClauses:
        counter = counter + 1
        new = reducedFoundClauses[counter]
        if new == node:
            continue
        #removes any litterals that have been used for reduction---------------------------------------------------
     #   unchanged = True
     #   for litteral in node.litterals:
     #       if litteral.reduced:
     #           node.litterals.remove(litteral)
     #           unchanged = False
     #   if node!= "":
     #       new.KB.append(node)
     #   if unchanged:
     #       continue
        # adds non reduced literals to KB of new
        restLitterals = []
        for litteral in node.litterals:
            if not litteral.reduced:
                restLitterals.append(litteral)
        if len(restLitterals) != 0:
            new.KB.append(Clause(restLitterals))
        #----------------------------------------------------------------------------------------------------------
        for i in range(len(reducedFoundClauses)):
            if i!=counter:
                new.KB.append(reducedFoundClauses[i])
        #Adds the difference between the lists.
        for clause1 in node.KB:
            addClause=True
            for clause2 in foundClauses:
                if clause1 == clause2 or clause1 in new.KB or clause1 == new:
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

        if backwardChaining(new,current_goals):
            return True

    if len(reducedFoundClauses) == 0:
        reducedFoundClauses = []
        for temp in node.KB:
            reducedNode = temp.reduced(node)
            if reducedNode != node and reducedNode != "":
                reducedFoundClauses.append(reducedNode)

        if len(reducedFoundClauses) == 0:
            return True

        for clause in reducedFoundClauses:

            clause.KB = reducedFoundClauses

            restLitterals = []
            for litteral in node.litterals:
                if not litteral.reduced:
                    restLitterals.append(litteral)
                if len(restLitterals) != 0:
                    clause.KB.append(Clause(restLitterals))

            if backwardChaining(clause, current_goals):
                return True

    return False


# sets up base case
createKB()
start = Clause([contradiction])
start.KB = KB
current_goals = []
current_goals.append(start)
print backwardChaining(start,current_goals)