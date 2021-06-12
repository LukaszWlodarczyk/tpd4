from Way import Way


class Node:
    def __init__(self, name):
        self.name = name

    def calculate_cost(self, ways):
        results = []
        for way in ways:
            if way.f_node == self:
                if way.s_node not in [way_tmp.f_node for way_tmp in ways]:
                    results.append(way.cost)
                else:
                    results.append(way.cost + way.s_node.calculate_cost(ways))
        return min(results)