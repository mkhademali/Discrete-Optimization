import networkx as nx

def select_unassigned_vertex(G, node_colors):
    # Select the vertex with the maximum degree of saturation
    # In case of a tie, the node with the higher degree is selected
    unassigned_nodes = [node for node in G.nodes if node not in node_colors]
    if not unassigned_nodes:
        return None

    max_degree_of_saturation = -1
    selected_node = unassigned_nodes[0]

    for node in unassigned_nodes:
        adjacent_colors = {node_colors.get(neighbour) for neighbour in G[node]}
        degree_of_saturation = len(adjacent_colors - {None})

        if degree_of_saturation > max_degree_of_saturation or \
           (degree_of_saturation == max_degree_of_saturation and G.degree[node] > G.degree[selected_node]):
            max_degree_of_saturation = degree_of_saturation
            selected_node = node

    return selected_node

def is_valid_color(G, node, color, node_colors):
    return all(color != node_colors.get(neighbour) for neighbour in G.neighbors(node))

def graph_coloring(G, node_colors, max_colors):
    node = select_unassigned_vertex(G, node_colors)
    if node is None:
        return True

    for color in range(1, max_colors + 1):
        if is_valid_color(G, node, color, node_colors):
            node_colors[node] = color
            if graph_coloring(G, node_colors, max_colors):
                return True
            node_colors.pop(node)

    return False

def solve_it(input_data):
    lines = input_data.split('\n')
    node_count, edge_count = map(int, lines[0].split())

    G = nx.Graph()
    G.add_nodes_from(range(node_count))
    for line in lines[1:edge_count + 1]:
        G.add_edge(*map(int, line.split()))

    node_colors = {}
    max_colors = 1

    while not graph_coloring(G, node_colors, max_colors):
        max_colors += 1
        node_colors = {}

    solution = [node_colors[node] for node in sorted(G.nodes())]

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(max_colors) + '\n'
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
