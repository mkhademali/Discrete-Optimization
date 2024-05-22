import numpy as np
from asyncore import read
from collections import namedtuple
from itertools import count
from trace import Trace

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])


def readfile(filename):
    with open(filename) as thefile:
        return thefile.read()


input_data = readfile('data/ks_10000_0')
# parse the input
lines = input_data.split('\n')
firstLine = lines[0].split()
item_count = int(firstLine[0])
capacity = int(firstLine[1])
items = []
for i in range(1, item_count+1):
    parts = lines[i].split()
    items.append(
        Item(i-1, int(parts[0]), int(parts[1]), int(parts[0])/int(parts[1])))

try:
    # Dynamic Programing
    O = np.zeros((capacity+1, item_count))
    for item in items:
        j = item.index
        for k in range(capacity+1):
            if k == 0:
                O[k][j] = 0
            elif item.weight <= k:
                O[k][j] = max(O[k][j-1], item.value + O[k-item.weight][j-1])
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
    # a greedy algorithm to produce a lower bownd
    print("Err")
    value = 0
    weight = 0
    taken = [0]*len(items)
    items.sort(key=lambda item: item.density, reverse=True)
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value

    X = taken
    O = value
print(X)
print(np.max(O))
