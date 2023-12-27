from visualize import visualize_graph

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def solve_part_one(filename):
    graph = {}
    lines = parse_input(filename)
    for line in lines:
        node, connections = line.split(": ")
        connections = connections.split(" ")
        
        if node not in graph.keys():
            graph[node] = []
        for connection in connections:
            if connection not in graph.keys():
                graph[connection] = []
            graph[node].append(connection)

    visualize_graph(graph)

solve_part_one("day25.txt")