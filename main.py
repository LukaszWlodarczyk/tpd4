from Node import Node
from Way import Way

nodes = list()
ways = list()


def create_n_nodes(n):
    nodes.append(Node('Blind'))
    for x in range(n):
        nodes.append(Node(x+1))


def create_way(name, cost, start, finish):
    new_way = Way(name, cost, start, finish)
    ways.append(new_way)


def print_best_path():
    path = []
    way_not_none = True
    path.append(str(nodes[-1].name))
    next_node = nodes[-1].best_way[0]
    while way_not_none:
        for node in nodes:
            if node.name == next_node:
                path.append(str(node.name))
                if node.best_way is None:
                    way_not_none = False
                else:
                    next_node = node.best_way[0]
    return path[::-1]


create_n_nodes(9)
create_way('A', 14, nodes[1], nodes[4])
create_way('B', 13, nodes[1], nodes[5])
create_way('C', 10, nodes[2], nodes[4])
create_way('D', 11, nodes[2], nodes[5])
create_way('E', 14, nodes[3], nodes[5])
create_way('F', 10, nodes[4], nodes[6])
create_way('G', 13, nodes[4], nodes[7])
create_way('H', 15, nodes[4], nodes[8])
create_way('I', 10, nodes[5], nodes[6])
create_way('J', 12, nodes[5], nodes[7])
create_way('K', 0, nodes[5], nodes[8])
create_way('L', 20, nodes[6], nodes[9])
create_way('M', 19, nodes[7], nodes[9])
create_way('N', 18, nodes[8], nodes[9])

print(f"The lowest cost: {nodes[-1].calculate_cost(ways)}")

# for node in nodes:
#     print(f"Node: {node.name} Way: {node.best_way} cost: {node.best_cost}")

print(f"The best path: {','.join(print_best_path())}")