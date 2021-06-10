from Node import Node
from State import State
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


create_n_nodes(10)
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
