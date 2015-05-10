from Litteral import *
from Clause import *

KB = []
contradiction = Litteral("a", False)
#contradiction = Clause([Litteral("n"), Litteral("h", False)])

# Knowledgebase
def createKB1():

    KB.append(Clause([Litteral("a"), Litteral("b", False)]))

    KB.append(Clause([Litteral("a"), Litteral("c", False)]))

    KB.append(Clause([Litteral("b"), Litteral("b", False)]))

    KB.append(Clause([Litteral("b"), Litteral("c", False)]))

    KB.append(Clause([Litteral("b"), Litteral("d", False)]))

    KB.append(Clause([Litteral("c")]))

    KB.append(Clause([Litteral("d")]))

    #KB.append(Clause([Litteral("a")]))
def createKB2():
    #Actural KB
    #water=w
    #OK-pump=k
    #On-pump = p
    #Man-fill = m
    #s = s
    #On-boiler = n
    #Ok-boiler = b
    #coffe = c
    #hot drink = h
    #Tea = t
    KB.append(Clause([Litteral("w"), Litteral("k", False)]))
    KB.append(Clause([Litteral("w"), Litteral("n", False)]))
    KB.append(Clause([Litteral("w"), Litteral("m", False)]))
    KB.append(Clause([Litteral("m"), Litteral("n")]))
    KB.append(Clause([Litteral("m"), Litteral("n")]))
    KB.append(Clause([Litteral("w", False), Litteral("s")]))
    KB.append(Clause([Litteral("b", False), Litteral("s")]))
    KB.append(Clause([Litteral("n", False), Litteral("s")]))
    KB.append(Clause([Litteral("s", False), Litteral("w", False)]))
    KB.append(Clause([Litteral("w", False), Litteral("s")]))
    KB.append(Clause([Litteral("n"), Litteral("s", False)]))
    KB.append(Clause([Litteral("b"), Litteral("s", False)]))
    KB.append(Clause([Litteral("s", False), Litteral("h")]))
    KB.append(Clause([Litteral("c", False), Litteral("h")]))
    KB.append(Clause([Litteral("s", False), Litteral("h")]))
    KB.append(Clause([Litteral("t", False), Litteral("h")]))
    KB.append(Clause([Litteral("c"), Litteral("t")]))

    #contradiction
    KB.append(Clause([Litteral("k"), Litteral("h", False)]))
   # KB.append(Clause([Litteral("n"), Litteral("h", False)]))

def backwardChaining(node,current_goals):
    print(node)
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
                KB.remove(cl)
                i=i-1
        i = i+1
    #remove reduced litterals from node
    i = 0
    while i < len(node.litterals):
        if node.litterals[i].reduced:
            node.litterals.pop(i)
            i=i-1
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
        if new == node:
            current_goals.remove(new)
            continue
        new.KB = node.KB
        if(backwardChaining(new,current_goals)):
            return True
    return False

# sets up base case
createKB1()
#createKB2()
start = Clause([contradiction])
#start=contradiction
start.KB = KB
current_goals = []
current_goals.append(start)
print backwardChaining(start,current_goals)