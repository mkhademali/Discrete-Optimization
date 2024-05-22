#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from ortools.sat.python import cp_model


def solve_it(input_data):
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

    # OR tools
    # list of colors to nodes initialized with 0
    solution = [0] * (node_count)

    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    for i in range(node_count):
        solution[i] = model.NewIntVar(0, int(node_count), '')
        
    # Adds  constraint
    for edge in edges:
        model.Add(solution[edge[0]] != solution[edge[1]])

    # Create the objective function
    obj_var = model.NewIntVar(0, node_count, 'makespan')
    model.AddMaxEquality(obj_var,solution)
    model.Minimize(obj_var)

    #ortools
    obj, is_optimal, solution = solver(node_count, edge_count, edge, max_minutes=1)

    output_data = str(obj) + ' ' + str(is_optimal) + '\n'
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
