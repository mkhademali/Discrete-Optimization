#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from collections import deque


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    # My CP solution
    # Nodes Adjacency
    NodesAdjacentTo = [set() for i in range(node_count)]
    for i in range(node_count):
        for e in edges:
            if {i} & set(e) != set():
                NodesAdjacentTo[i] = NodesAdjacentTo[i] | set(e)
        NodesAdjacentTo[i].remove(i)
    # Finding the most dense nodes: Dictionary version
    NodesDegree = {}
    for i in range(edge_count):
        NodesDegree[edges[i][0]] = 0
        NodesDegree[edges[i][1]] = 0
    for i in range(edge_count):
        NodesDegree[edges[i][0]] += 1
        NodesDegree[edges[i][1]] += 1
    SortedNodesDegree = sorted(
        NodesDegree, key=lambda value: NodesDegree[value], reverse=True)

    # Variable: Node Color
    NodesColor = dict()
    # Domain : Availible colors for each node
    NodesDomain = [deque([i for i in range(0, node_count)]) for i in range(
        0, node_count)]
    # Stack of nodes to be colored
    UncoloredNodes = deque({i for i in range(node_count)})
    # FirstNodeToBeColored
    i = SortedNodesDegree[0]
    c = 0
    NodesColor[i] = c
    # Remove colored node from stack
    UncoloredNodes.remove(i)
    # Remove assigned color from domains of adjacent nodes
    for j in NodesAdjacentTo[i]:
        NodesDomain[j].remove(c)

    while True:
        i = UncoloredNodes[0]
        c = NodesDomain[i][0]
        NodesColor[i] = c
        UncoloredNodes.remove(i)
        if UncoloredNodes == deque([]):
            break
        for j in NodesAdjacentTo[i]:
            if NodesDomain[j].count(c) == 1:
                NodesDomain[j].remove(c)
    solution = list(dict(sorted(NodesColor.items())).values())

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
