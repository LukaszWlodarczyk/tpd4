import numpy as np


class Node:
    def __init__(self, name):
        self.name = name
        self.best_way = None
        self.best_cost = None

    def calculate_cost(self, ways):
        results = []
        paths = []
        for way in ways:
            if way.f_node == self:
                if way.s_node not in [way_tmp.f_node for way_tmp in ways]:
                    results.append(way.cost)
                    paths.append((way.s_node.name, way.f_node.name))
                else:
                    results.append(way.cost + way.s_node.calculate_cost(ways))
                    paths.append((way.s_node.name, way.f_node.name))
        min_value = np.Inf
        min_iter = None
        for iter, value in enumerate(results):
            if value < min_value:
                min_value = value
                min_iter = iter
        self.best_cost = min_value
        self.best_way = paths[min_iter]
        return min_value
        # return min(results)