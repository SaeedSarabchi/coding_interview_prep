class GraphNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def has_route(self, src_node, dst_node):
        visited = set()
        visited.add(src_node)
        if dst_node in visited:
            return True
        for c in src_node.children:
            if c == dst_node:
                return True
            return self.recursive_has_route(c, dst_node, visited)
        return False

    def recursive_has_route(self, curr_node, dst_node, visited):
        visited.add(curr_node)
        for c in curr_node.children:
            if c not in visited:
                if c == dst_node:
                    return True
                return self.recursive_has_route(c, dst_node, visited)
        return False


node_a = GraphNode(1)
node_b = GraphNode(2)
node_c = GraphNode(3)
node_a.children = [node_b]
node_b.children = [node_c]

g = Graph([node_a, node_b, node_c])
print(g.has_route(node_b, node_a))

node_0 = GraphNode(0)
node_1 = GraphNode(1)
node_2 = GraphNode(2)
node_3 = GraphNode(3)
node_4 = GraphNode(4)
node_0.children = [node_1, node_3]
node_0.child_weights = [2, 1]
node_1.children = [node_2]
node_1.child_weights = [2]
node_2.children = [node_4]
node_2.child_weights = [4]
node_3.children = [node_4]
node_3.child_weights = [1]
node_4.children = [node_2]
node_4.child_weights = [1]
graph = Graph([node_0, node_1, node_2, node_3, node_4])
print(g.has_route(node_1, node_4))