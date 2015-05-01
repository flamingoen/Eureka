from Litteral import Litteral
KB = [[]]
contradiction = Litteral(False,"a")
#Knowledgebase
def CreateKB(contradiction):

    KB[0].append(contradiction)

    KB[1].append(Litteral("a"))
    KB[1].append(Litteral(False,"b"))

    KB[2].append(Litteral("a"))
    KB[2].append(Litteral(False,"c"))

    KB[3].append(Litteral("b"))
    KB[3].append(Litteral(False,"c"))

    KB[4].append(Litteral("b"))
    KB[4].append(Litteral(False,"d"))

    KB[5].append(Litteral("c"))

    KB[6].append(Litteral("d"))
CreateKB(contradiction)



