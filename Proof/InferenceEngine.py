from Litteral import Litteral
from Clause import Clause

KB = []
contradiction = Litteral("a",False)


#Knowledgebase
def CreateKB(contradiction):

    KB.append(Clause([contradiction]))

    KB.append(Clause([Litteral("a"), Litteral("b",False)]))

    KB.append(Clause([Litteral("a"), Litteral("c",False)]))

    KB.append(Clause([Litteral("b"), Litteral("b",False)]))

    KB.append(Clause([Litteral("b"), Litteral("c",False)]))

    KB.append(Clause([Litteral("b"), Litteral("c",False)]))

    KB.append(Clause([Litteral("c")]))

    KB.append(Clause([Litteral("d")]))


def calcKB(clause):
    for kb1 in clause.KB:
        for literal_1 in kb1:
            kb1remove = False
            for kb2 in clause.KB:
                if kb1 == kb2:
                    continue
                for literal_2 in kb2:
                    if literal_2 == literal_1:
                        kb1remove = True
                    elif literal_2.char == literal_1.char:
                        kb1remove = True
                        kb2.remove(literal_2)
                        clause.KB = filter(None, clause.KB)
            if kb1remove:
                kb1.remove(literal_1)
                clause.KB = filter(None, clause.KB)

    i = 0 # What is this??
    for neighbour in clause.neighbours:
        neighbour.KB.append(clause.KB[i])
        i=i+1


# Program:

# construct test KB
CreateKB(contradiction)

# initialize the map of clauses
for clause in KB:
    for neighbour in KB:
        nbool = False
        if neighbour == clause:
            continue
        for lit in clause.litterals:
            if nbool:
                break

            for l in neighbour.litterals:
                if(l.char == lit.char):
                    clause.neighbours.append(neighbour)
                    nbool = True
                    break

# adds the contradiction to the map
KB[0].KB.append([contradiction])
for neighbour in KB[0].neighbours:
    KB[0].KB.append(neighbour.litterals)

calcKB(KB[0])


print "hello world!"