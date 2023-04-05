import nodeEdges 

class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children

    def __init__(self):
        self._nodes = []
        self._edges = {}

    def add_node(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate Node')
        else:
            self._nodes.append(node)
            self._edges[node]= []

    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError('Node not in the graphp')
        self._edges[src].append(dest)

    def children_of(self, node):
        return self._edges[node]
    def has_node(self, node):
        return node in self._nodes
    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest  in self._edges[src]:
                result = (result+src.get_name()+'-->'+dest.get_name()+'\n')
        return result[:-1]

class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = nodeEdges.Edge(edge.get_destination(), edge.get_source()) 
        Digraph.add_edge(self, rev)

graph1 = Digraph()
na=nodeEdges.Node('a')
graph1.add_node(na)
nb=nodeEdges.Node('b')
graph1.add_node(nb)
nc=nodeEdges.Node('c')
graph1.add_node(nc)
nd=nodeEdges.Node('d')
graph1.add_node(nd)
graph1.add_edge(nodeEdges.Edge(na,nb))
graph1.add_edge(nodeEdges.Edge(na,nd))
graph1.add_edge(nodeEdges.Edge(na,nc))
print(graph1)


