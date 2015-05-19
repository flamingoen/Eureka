from NodeGenerator import *

nodes = nodeGenerator()
def gen_wrapper(cmp):
    class Wrapper(object):
        def __init__(self, value): self.value = value
        def __cmp__(self, obj): return cmp(self.value, obj.value)
    return Wrapper


def eureka(start, goal):
    nodes = nodeGenerator()
    closed_list = []
    open_list = [start]
    start.parent.append(Node(-1,-1))

   # open_list.append(start)

    while len(open_list)>0:
        open_list.sort(key=lambda node: node.dist_from_start + node.calc_estimated_dist(goal), reverse=True)#f(n)=g(n)+h(n)
        current = open_list.pop()  # this should be done in a heap, but python wont let me do it!!

        if current == goal:
            print "GOAL!"
            s = current.parent[0].map[current]
            current = current.parent[0]
            while(current.parent[-1].x != -1 and current.parent[-1].y != -1):
                s = current.parent[0].map[current]+" "+ s
                current = current.parent[0]
            print s
            return

        closed_list.append(current)
        #open_list.remove(current)

        for neighbour in current.neighbours:
            if neighbour in closed_list:
                continue

            new_dist = current.dist_from_start + current.calc_estimated_dist(neighbour)

            if neighbour not in open_list or new_dist < neighbour.dist_from_start:
                neighbour.came_from = current
                neighbour.dist_from_start = new_dist
                neighbour.parent.append(current)
                neighbour.dist_estimated_to_finish = neighbour.dist_from_start + neighbour.calc_estimated_dist(goal)
                if neighbour not in open_list:
                    open_list.append(neighbour)
i=0
for node in nodes:
    print(i,". x= ",node.x," y= ",node.y, " Neighbours: ")
    for n in node.neighbours:
        print("          x= ",n.x," y= ",n.y)
    i=i+1

eureka(nodes[0], nodes[11])
print("done")
