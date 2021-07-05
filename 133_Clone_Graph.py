
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return None
    total_graph = {}
    # a helper that creates / clones all the vertices of the graph
    def create_clones(subgraph):
        if subgraph.val in total_graph:
            pass
        else: 
            total_graph[subgraph.val] = Node(subgraph.val)
        for i in range(len(subgraph.neighbors)):
            if subgraph.neighbors[i].val not in total_graph:
                create_clones(subgraph.neighbors[i])        
    create_clones(node)
    finished = {}
    
    # a helper that clones the neighbors of all the vertices
    def clone_edges(vertex):
        if vertex.val in finished:
            pass
        else: 
            for i in range(len(vertex.neighbors)):
                total_graph[vertex.val].neighbors.append(total_graph[vertex.neighbors[i].val])       
            finished[vertex.val] = "whatever dude"
            for i in range(len(vertex.neighbors)):
                if vertex.neighbors[i].val not in finished:
                    clone_edges(vertex.neighbors[i])
    clone_edges(node)
    return total_graph[1]
