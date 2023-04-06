import depthFirstSearch
import digraphGraph
import nodeEdges

def BFS(graph, start, end, to_print=False):
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue)!=0:
        #remove oldest element in path_queue
        tmp_path = path_queue.pop(0)
        if to_print:
            print('Currente BFS path :', depthFirstSearch.print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        #
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:#evita ciclo
                new_path = tmp_path+[next_node]
                path_queue.append(new_path)
    return None

def test_SP():
    nodes = []
    for name in range(6):
        nodes.append(nodeEdges.Node(str(name)))
    g =digraphGraph.Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(nodeEdges.Edge(nodes[0],nodes[1]))
    g.add_edge(nodeEdges.Edge(nodes[1],nodes[2]))
    g.add_edge(nodeEdges.Edge(nodes[2],nodes[3]))
    g.add_edge(nodeEdges.Edge(nodes[2],nodes[4]))
    g.add_edge(nodeEdges.Edge(nodes[3],nodes[4]))
    g.add_edge(nodeEdges.Edge(nodes[3],nodes[5]))
    g.add_edge(nodeEdges.Edge(nodes[0],nodes[2]))
    g.add_edge(nodeEdges.Edge(nodes[1],nodes[0]))
    g.add_edge(nodeEdges.Edge(nodes[3],nodes[1]))
    g.add_edge(nodeEdges.Edge(nodes[4],nodes[0]))

    sp = BFS(g,nodes[0],nodes[5],True)
    print('Shortest path  foundn by BFS ', depthFirstSearch.print_path(sp))

test_SP()


