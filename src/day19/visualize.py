import graphviz

def visualize_graph(graph):
    dot = graphviz.Graph('connections', format='png')  

    # Loop over graph to add all nodes
    for node in graph.keys():
        dot.node(node)

    for node in graph.keys():
        for connection in graph[node]:
            if type(connection) == tuple:
                dot.edge(node, connection[1], label=connection[0])
            else:
                dot.edge(node, connection)

    dot.view()