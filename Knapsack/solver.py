#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])


def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(
            Item(i-1, int(parts[0]), int(parts[1]), int(parts[0])/int(parts[1])))
    try:
        # Dynamic Programing
        O = np.zeros((capacity+1, item_count), dtype=int)
        for item in items:
            j = item.index
            for k in range(capacity+1):
                if k == 0:
                    O[k][j] = 0
                elif item.weight <= k:
                    O[k][j] = max(O[k][j-1], item.value +
                                  O[k-item.weight][j-1])
                else:
                    O[k][j] = O[k][j-1]
        X = np.zeros(item_count, dtype=int)
        k = capacity
        for j in range(item_count-1, 0, -1):
            if O[k][j] > O[k][j-1]:
                X[j] = 1
                k = k - items[j].weight
                if k <= 0:
                    break
            j = j - 1
    except ValueError:
        # Vectorized version of input
        V = np.zeros(item_count, dtype=int)  # Values
        W = np.zeros(item_count, dtype=int)  # Weights
        for i in range(1, item_count+1):
            parts = lines[i].split()
            V[i-1] = (int(parts[0]))
            W[i-1] = (int(parts[1]))
        # My BnB
        NodeVal = 0
        NodeWei = 0
        Counter = 0
        LowerBound = 0
        X_BestFound = 0
        # DFS
        for j in range(item_count-1):
            X = np.zeros(item_count, dtype=int)
            for i in range(j, item_count):
                Counter += 1
                X[i] = 1
                if np.dot(X, W) <= capacity:   # Feasibility Check
                    NodeVal = np.dot(X, V)
                    NodeWei = np.dot(X, W)
                else:
                    break
            if NodeVal >= LowerBound:
                LowerBound = NodeVal
                X_BestFound = X
        O = int(LowerBound)
        X = X_BestFound
    # prepare the solution in the specified output format
    output_data = str(np.max(O)) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, X))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
