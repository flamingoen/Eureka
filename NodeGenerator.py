from Node import Node

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
    bol_previous_node = False
    #Load file
    with open("copenhagen_streetmap.txt") as inputfile:
        for line in inputfile:
            temp.append(line.strip().split())
    #Creates pair nodes
    pair = False
    for t in temp:
        for value in t:
            #For all words read from the text document
            #print (value)
            if is_number(value):
                #print "value"
                if pair:
                    y = int(value)
                    #print("pair")
                    current_node = Node(x,y)
                     #Add neightbours
                    if bol_previous_node:
                        previous_node.neighbours.append(current_node)
                        bol_previous_node = False
                    else:
                        bol_previous_node = True
                    #Add new node to list
                    newNode = True
                    for node in nodes:
                        if(node.x == x and node.y == y):
                            current_node=node
                            newNode = False
                    if newNode:
                        nodes.append(current_node)
                    pair = False
                    previous_node = current_node
                else:
                    x = int(value)
                    pair = True

    return nodes
#"main"
nodes = nodeGenerator()
for node in nodes:
    print("x= ",node.x," y= ",node.y, " Neighbours: ")
    for n in node.neighbours:
        print("          x= ",n.x," y= ",n.y)