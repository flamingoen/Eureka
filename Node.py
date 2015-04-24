import math


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.map =  {}
        #self.came_from
        self.neighbours = []
        self.dist_from_start = 0
        self.dist_estimated_to_finish = 0

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def calc_estimated_dist(self, node):
        #return math.sqrt(self.x-*node.x+self.y*node.y)
        return math.sqrt(((self.x-node.x)*(self.x-node.x))+((self.y-node.y)*(self.y-node.y)))

    def add_neighbour(self, node):
        self.neigbours.append(node)
    def __hash__(self):
        return hash((self.x, self.y))