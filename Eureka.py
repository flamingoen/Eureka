import Node


def gen_wrapper(cmp):
    class Wrapper(object):
        def __init__(self, value): self.value = value
        def __cmp__(self, obj): return cmp(self.value, obj.value)
    return Wrapper


def eureka(start, goal):
    closed_list = []
    open_list = []

    open_list.append(start)

    while not open_list:
        open_list.sort(key=lambda node: node.dist_estimated_to_finish, reverse=True)
        current = open_list.pop()  # det her burde gøres i en heap, men python vil ikke lade mig gøre det!!!

        if current == goal:
            return goal.dist_from_start

        closed_list.append(current)
        open_list.remove(current)

        for neighbor in current.neighbors:
            if neighbor in closed_list:
                continue

            new_dist = current.dist_from_start + current.calc_estimated_dist(neighbor)

            if neighbor not in open_list or new_dist < neighbor.dist_from_start:
                neighbor.came_from = current
                neighbor.dist_from_start = new_dist
                neighbor.dist_estimated_to_finish = neighbor.dist_from_start + neighbor.calc_estimated_dist(goal)
                if neighbor not in open_list:
                    open_list.append(neighbor)