from collections import deque


def readfile(filename):
    with open(filename) as thefile:
        return thefile.read()


input_data = readfile('data/gc_4_1')
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

# Nodes Adjacency
NodesAdjacentTo = [set() for i in range(node_count)]
for i in range(node_count):
    for e in edges:
        if {i} & set(e) != set():
            NodesAdjacentTo[i] = NodesAdjacentTo[i] | set(e)
    NodesAdjacentTo[i].remove(i)
print('Nodes Adjacency', NodesAdjacentTo)

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
NodesColor = {}
# Domain : Availible colors for each node
NodesDomain = [deque([i for i in range(0, node_count)]) for i in range(
    0, node_count)]

# Stack of nodes to be colored
UncoloredNodes = deque({i for i in range(node_count)})
print('all nodes to be colored are', UncoloredNodes)
# FirstNodeToBeColored
i = SortedNodesDegree[0]
c = 0
NodesColor[i] = c
print('first, assign color', c, 'to node', i)
# Remove colored node from stack
print('remove node', i, 'from Uncolored list')
UncoloredNodes.remove(i)
# Remove assigned color from domains of adjacent nodes
print('Now remove the assigned color', c,
      'from domain of adjacent nodes to node', i, 'which are', NodesAdjacentTo[i])

for j in NodesAdjacentTo[i]:
    print('Then node', j, 'has domain:',
          NodesDomain[j], 'and we need to remove color', c, 'from it')
    NodesDomain[j].remove(c)
    print('now the domain of node', j, 'is', NodesDomain[j])


print('Now the while loop')
while True:
    print('remained uncolored nodes', UncoloredNodes)
    i = UncoloredNodes[0]
    print('node to be colored', i)
    c = NodesDomain[i][0]
    print('choose first color from this node domain:', c)
    NodesColor[i] = c
    print('assign color', c, 'to node', i)
    print('pop this colored node')
    UncoloredNodes.remove(i)
    if UncoloredNodes == deque([]):
        print('XXXXXXXXXXXXXXXX')
        print(NodesColor)
        print(max(NodesColor.values())+1)
        break
    print('UncoloredNodes', UncoloredNodes)
    for j in NodesAdjacentTo[i]:
        print('okey node', j, 'has domain:',
              NodesDomain[j], 'and we need to remove color', c, 'from it')
        print('****There are ')
        if NodesDomain[j].count(c) == 1:
            print(c, 'was in', NodesDomain[j])
            NodesDomain[j].remove(c)
            print("I have removed it")
        else:
            print('no', c, 'wasnt')
        print('now the domain of node', j, 'is', NodesDomain[j])
