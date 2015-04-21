import Node
#function to check if it is a number
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def nodeGenerator() :
    temp = []
    nodes = []
    x = 0
    y = 0
    #Load file
    with open("copenhagen_streetmap.txt") as inputfile:
        for line in inputfile:
            temp.append(line.strip().split())
    #Creates pair nodes
    pair = False
    for t in temp:
        for value in t:
            print (value)
            if is_number(value):
                print "value"
                if pair:
                    y = int(value)
                    print("pair")
                    nodes.append(Node(x,y))
                    return
                    pair = False
                else:
                    x = int(value)
                    pair = True
    print len(nodes)
    return

nodeGenerator()