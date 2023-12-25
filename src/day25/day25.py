from visualize import visualize_graph

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one(filename):
    graph = []
    lines = parse_input(filename)
    for line in lines:
        node, connections = line.split(": ")
        connections = connections.split(" ")
        graph.append((node, connections))
    visualize_graph(graph)

solve_part_one("day25.txt")