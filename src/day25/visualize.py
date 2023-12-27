import graphviz

def visualize_graph(graph):
    dot = graphviz.Graph('connections')  

    # Loop over graph to add all nodes
    for node in graph.keys():
        dot.node(node)

    for node in graph.keys():
        for connection in graph[node]:
            dot.edge(node, connection)

    dot.view()