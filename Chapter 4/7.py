from Graph import Graph, GraphNode


def topological_sort(graph):
    visited = set()
    # time = 0
    sorted_graph = []
    for node in graph.nodes:
        if node not in visited:
            dfs(node, visited, sorted_graph)
        else:
            if node not in sorted_graph:
                raise Exception("Error, there is a loop")
    return sorted_graph


def dfs(node, visited, sorted_graph):
    # time = time + 1
    # node.start = time
    visited.add(node)
    for child in node.children:
        if child not in visited:
            # traverse the child
            dfs(child, visited, sorted_graph)
        else:
            if child not in sorted_graph:
                raise Exception("Error, there is a loop")
    # time = time + 1
    # node.finish = time
    sorted_graph.insert(0, node)


graph = Graph()
node_a = GraphNode("a")
node_b = GraphNode("b")
node_c = GraphNode("c")
node_d = GraphNode("d")
node_e = GraphNode("e")
node_f = GraphNode("f")
node_a.children = [node_d]
node_b.children = [node_d]
node_f.children = [node_a, node_b]
node_d.children = [node_c]
graph.nodes = [node_a, node_b, node_c, node_d, node_e, node_f]
res = topological_sort(graph)
print(res)
