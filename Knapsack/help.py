from asyncore import read
from collections import namedtuple
from itertools import count
from trace import Trace

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])


def readfile(filename):
    with open(filename) as thefile:
        return thefile.read()


input_data = readfile('data/ks_4_0')

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

value = 0
weight = 0
taken = [0]*len(items)

# a greedy algorithm to produce a lower bownd
items.sort(key=lambda item: item.density, reverse=True)
for item in items:
    if weight + item.weight <= capacity:
        taken[item.index] = 1
        value += item.value
        weight += item.weight

local_solution = taken
lower_bound = value


# print(items)
print('taken1:', taken)
print('value1:', value)
print('capacity1:', capacity)
print('weight1:', weight)

# local search
counted_branches = local_solution.count(0)

while counted_branches > 0:
    a = taken.index(1)
    b = taken.index(0)
    taken[taken.index(1)] = 0
    taken[taken.index(0)] = 1
    value = value + items[b].value - items[a].value
    weight = weight + items[b].weight - items[a].weight
    if value >= lower_bound and weight <= capacity:
        lower_bound = value
        local_solution = taken
    counted_branches -= 1

print('taken2:', local_solution)
print('value2:', lower_bound)
print('capacity2:', capacity)
print('weight2:', weight)

# del items
# del item


# relax the capacity constraint
# drop out the lowest value ons until the capacity constraint is met
