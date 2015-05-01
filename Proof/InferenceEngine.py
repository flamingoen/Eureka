from Litteral import Litteral
from Clause import Clause

KB = []
contradiction = Litteral("a",False)
#Knowledgebase
def CreateKB(contradiction):

    KB.append(Clause([contradiction]))

    KB.append(Clause([Litteral("a"),Litteral("b",False)]))

    KB.append(Clause([Litteral("a"),Litteral("c",False)]))

    KB.append(Clause([Litteral("b"),Litteral("b",False)]))

    KB.append(Clause([Litteral("b"),Litteral("c",False)]))

    KB.append(Clause([Litteral("b"),Litteral("c",False)]))

    KB.append(Clause([Litteral("c")]))

    KB.append(Clause([Litteral("d")]))

CreateKB(contradiction)


def calcKB(clause):
    for kb1 in clause.KB:
        for l1 in kb1:
            kb1remove = False
            for kb2 in clause.KB:
                if kb1 == kb2:
                    continue
                for l2 in kb2:
                    if l2 == l1:
                        kb1remove = True
                    elif l2.char == l1.char:
                        kb1remove = True
                        kb2.remove(l2)
                        clause.KB = filter(None, clause.KB)
            if kb1remove:
                kb1.remove(l1)
                clause.KB = filter(None, clause.KB)
    i = 0
    for neighbour in clause.neighbours:
        neighbour.KB.append(clause.KB[i])



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

KB[0].KB.append([contradiction])
for neighbour in KB[0].neighbours:
    KB[0].KB.append(neighbour.litterals)

clause = KB[0]
calcKB(clause)


print "hello world!"




