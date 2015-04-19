import math
class Node:

    neighbours = []
    dist_from_start = 0
    dist_estimated_to_finish = 0

    def __init__(self):
        self.x
        self.y

    def calc_estimated_dist(self,node):
        math.sqrt(self.x*node.x+self.y*node.y)