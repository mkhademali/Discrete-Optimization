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

# # All in One tuple version of input
# items = []
# for i in range(1, item_count+1):
#     parts = lines[i].split()
#     items.append(
#         Item(i-1, int(parts[0]), int(parts[1]), int(parts[0])/int(parts[1])))

# Vectorized version of input
V = np.zeros(item_count, dtype=int)  # Values
W = np.zeros(item_count, dtype=int)  # Weights
D = np.zeros(item_count, dtype=float)  # Densities
for i in range(1, item_count+1):
    parts = lines[i].split()
    V[i-1] = (int(parts[0]))
    W[i-1] = (int(parts[1]))
    D[i-1] = (int(parts[0])/int(parts[1]))

# the indecies of Density of items in a decsending order
DensityOrders = np.argsort(D)[::-1]
WS = W[DensityOrders]
VS = V[DensityOrders]
# items.sort(key=lambda item: item.density, reverse=True)

# Kvalue = 0
# Kweight = 0
# X0 = np.zeros(item_count)

# # a greedy algorithm to produce a lower bownd
# for i in range(item_count):
#     if Kweight + WS[i] <= capacity:
#         X0[DensityOrders[i]] = 1
#         Kvalue += VS[i]
#         Kweight += WS[i]

# LowerBound = Kvalue
# UpperBound = np.inf

# print(LowerBound, X0)
# My BnB
NodeVal = 0
NodeWei = 0
Counter = 0
LowerBound = 0
X_BestFound = 0
# DFS
for j in range(item_count-1):
    X = np.zeros(item_count)
    for i in range(j, item_count):
        Counter += 1
        X[i] = 1
        if np.dot(X, W) <= capacity:   # Feasibility Check
            NodeVal = np.dot(X, V)
            NodeWei = np.dot(X, W)
            # print(NodeVal, NodeWei)
        else:
            # print('breaked in', NodeVal, NodeWei, X)
            break
    if NodeVal >= LowerBound:
        LowerBound = NodeVal
        X_BestFound = X
print(Counter, LowerBound, X_BestFound)
