from pyvis import network as net

def parse_input(filename):
    return [line.strip('\n') for line in open(filename, 'r')]

def visualize_graph(graph):
    netw = net.Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    # Loop over graph to add all nodes
    for entry in graph:
        node, connections = entry
        netw.add_node(node)
        for connection in connections:
            netw.add_node(connection)
            netw.add_edge(node, connection)
           
    netw.show('graph.html', notebook=False)
    pass

def solve_part_one(filename):
    graph = []
    lines = parse_input(filename)
    for line in lines:
        node, connections = line.split(": ")
        connections = connections.split(" ")
        graph.append((node, connections))
    visualize_graph(graph)

solve_part_one("day25_test.txt")