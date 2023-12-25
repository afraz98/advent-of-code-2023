from pyvis import network as net

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
    pass'