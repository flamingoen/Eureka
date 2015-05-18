from Litteral import *
from Clause import *

KB = []
contradiction = Litteral("a", False)
#contradiction = Clause([Litteral("n"), Litteral("h", False)])

# Knowledgebase
def createKB():

    KB.append(Clause([Litteral("a"), Litteral("b", False)]))

    KB.append(Clause([Litteral("a"), Litteral("c", False)]))

    KB.append(Clause([Litteral("b"), Litteral("b", False)]))

    KB.append(Clause([Litteral("b"), Litteral("c", False)]))

    KB.append(Clause([Litteral("b"), Litteral("d", False)]))

    KB.append(Clause([Litteral("d")]))

    KB.append(Clause([Litteral("d")]))


def backwardChaining(node,cg):
    print(node)
    current_goals = list(cg)
    foundClauses = []
    # finding clause matching node
    i = 0
    while i < len(node.KB):
        cl = node.KB[i]
        for litteral in node.litterals:
            if (cl.contains(litteral)) and cl != node:
                clause = cl.reduced(node)
                if clause != node and clause != "":
                    foundClauses.append(clause)
                node.KB.pop(i)
                i=i-1
        i = i+1
    #remove reduced litterals from node
    i = 0
    while i < len(node.litterals):
        if node.litterals[i].reduced:
            node.litterals.pop(i)
            i=i-1
        else:
            return False
        i+=1
    if len(node.litterals)==0:
        current_goals.remove(node)

    # add clauses to current_goal
    for clause in foundClauses:
        isNewGoal = True
        for goal in current_goals:
            if clause == goal:
                isNewGoal = False
        if isNewGoal:
            current_goals.append(clause)

    #check for emptyness
    if(len(current_goals)==0):
        return True

    #run the recursion
    for clause in current_goals:
        new = clause
        if new == node or len(new.litterals)==0:
            current_goals.remove(new)
            continue
        new.KB = list(node.KB)
        if(backwardChaining(new,current_goals)):
            return True
        print("new branch")
    return False

# sets up base case
createKB()
start = Clause([contradiction])
start.KB = KB
cg = []
cg.append(start)
print backwardChaining(start,cg)