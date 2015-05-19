import math


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = []
        self.map =  {} #Key = other node, value = road between nodes
        self.neighbours = []
        self.dist_from_start = 0 #g(n)
        self.dist_estimated_to_finish = 0 #h(n)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.map == other.map)

    def calc_estimated_dist(self, node):
        #return math.sqrt(self.x-*node.x+self.y*node.y)
        return math.sqrt(((self.x-node.x)*(self.x-node.x))+((self.y-node.y)*(self.y-node.y)))

    def add_neighbour(self, node):
        self.neigbours.append(node)
    def __hash__(self):
        return hash((self.x, self.y))