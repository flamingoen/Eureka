import math


class Node:

    neighbours = []
    dist_from_start = 0
    dist_estimated_to_finish = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_estimated_dist(self, node):
        self.dist_estimated_to_finish = math.sqrt(self.x*node.x+self.y*node.y)

    def add_neighbour(self, node):
        self.neigbours.append(node)