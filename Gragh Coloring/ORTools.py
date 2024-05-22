from ortools.sat.python import cp_model

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


# list of colors to nodes initialized with 0
solution = [0] * (node_count)

# Instantiate the CpModel
model = cp_model.CpModel()

# Creates the variables.
for i in range(node_count):
    solution[i] = model.NewIntVar(0, int(node_count), '')
    
# Adds  constraint(i.e value of node A != value of node B) for each edge.
for edge in edges:
    model.Add(solution[edge[0]] != solution[edge[1]])

# Instantiate a Cp solver
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    colors = [solver.Value(solution[i]) for i in range(node_count)]

solution = colors



# Add a connection for each edge.
edges = [
               (0, 1),
               (1, 2),
               (2, 3),
               (3, 4),
               (0, 4),
               (1, 5),
               (0, 6),
               (2, 7),
               (3, 8),
               (4, 9),
               (5, 9),
               (5, 8),
               (6, 7),
               (6, 8),
               (7, 9)
]


print(colors)