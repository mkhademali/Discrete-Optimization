from ortools.sat.python import cp_model
import networkx as nx

def graph_coloring(input_data):
    # Parse the input
    lines = input_data.split('\n')
    node_count, edge_count = map(int, lines[0].split())
    max_colors = edge_count
    
    # Create graph using NetworkX
    G = nx.Graph()
    G.add_nodes_from(range(node_count))
    for line in lines[1:edge_count + 1]:
        G.add_edge(*map(int, line.split()))



    model = cp_model.CpModel()

    # Create a color variable for each node in the graph
    color_vars = {node: model.NewIntVar(0, max_colors - 1, f'color_of_{node}') for node in G.nodes}

    # Add constraints: adjacent nodes must have different colors
    for edge in G.edges:
        model.Add(color_vars[edge[0]] != color_vars[edge[1]])

    # Objective: Minimize the number of colors used
    max_color_used = model.NewIntVar(0, max_colors - 1, 'max_color_used')
    model.AddMaxEquality(max_color_used, list(color_vars.values()))
    model.Minimize(max_color_used)

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = [solver.Value(color_vars[node]) for node in G.nodes()]

    # Prepare the solution in the specified output format
    output_data = f"{node_count, solver.Value(max_color_used) + 1} \n" + ' '.join(map(str, solution))

    return output_data
# Example usage

def readfile(filename):
    with open(filename) as thefile:
        return thefile.read()

input_data = readfile('data/gc_20_1')
print(graph_coloring(input_data))