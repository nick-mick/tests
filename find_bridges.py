# pseudocode

graph = Graph() # initialisation graph - Graph class object

def find_briges(self)        # method of class Graph
    bridges = [] 
    for edge in self.edges    # going through all edges in loop 
        edge_buffer = edge      # to remember edge before removing from graph
        remove_edge(edge)        # method for removing edge from graph
        if not is_connected(self)     # metod for checking if graph remains connected
            bridges.append(edge)    # if False add edge to bridges
        self.add_edge(edge_buffer)  # return edge to graph from buffer
    return bridges 
            


