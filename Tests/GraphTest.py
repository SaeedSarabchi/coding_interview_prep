import unittest
from Graph import Graph, GraphNode


class TestGraph(unittest.TestCase):
    def init_graph(self):
        self.graph = Graph()
        node_0 = GraphNode(0)
        node_1 = GraphNode(1)
        node_2 = GraphNode(2)
        node_3 = GraphNode(3)
        node_4 = GraphNode(4)
        node_5 = GraphNode(5)
        node_0.children = [node_1, node_4, node_5]
        node_1.children = [node_3, node_4]
        node_2.children = [node_1]
        node_3.children = [node_2, node_4]
        self.graph.nodes = [node_0, node_1, node_2, node_3, node_4, node_5]

    def test_dfs(self):
        self.init_graph()
        self.assertEqual(self.graph.dfs(), [0,1,3,2,4,5])

    def test_bfs(self):
        self.init_graph()
        self.assertEqual(self.graph.bfs(), [0,1,4,5,3,2])

    def test_bi_directional_search(self):
        self.graph = Graph()
        node_0 = GraphNode(0)
        node_1 = GraphNode(1)
        node_2 = GraphNode(2)
        node_3 = GraphNode(3)
        node_4 = GraphNode(4)
        node_5 = GraphNode(5)
        node_6 = GraphNode(6)
        node_0.children = [node_1, node_4, node_5]
        node_1.children = [node_3, node_4]
        node_2.children = [node_1, node_6]
        node_3.children = [node_2]
        node_4.children = [node_3]
        self.graph.nodes = [node_0, node_1, node_2, node_3, node_4, node_5, node_6]
        self.assertEqual(self.graph.bi_directional_search(self.graph.nodes[0], self.graph.nodes[6]), [0, 1, 3, 2, 6], "path 0->6")
        self.assertEqual(self.graph.bi_directional_search(self.graph.nodes[0], self.graph.nodes[2]), [0, 1, 3, 2], "path 0->2")

    def test_topological_sort(self):
        self.graph = Graph()
        node_undershorts = GraphNode("undershorts")
        node_pants = GraphNode("pants")
        node_belt = GraphNode("belt")
        node_shirt = GraphNode("shirt")
        node_tie = GraphNode("tie")
        node_jacket = GraphNode("jacket")
        node_socks = GraphNode("socks")
        node_shoes = GraphNode("shoes")
        node_watch = GraphNode("watch")
        node_undershorts.children = [node_pants, node_shoes]
        node_pants.children = [node_shoes, node_belt]
        node_belt.children = [node_jacket]
        node_shirt.children = [node_belt, node_tie]
        node_tie.children = [node_jacket]
        node_socks.children = [node_shoes]
        self.graph.nodes = [node_undershorts, node_pants, node_belt, node_shirt, node_tie, node_jacket, node_socks,
                            node_shoes, node_watch]
        self.assertEqual(self.graph.topological_sort(), ['watch', 'socks', 'shirt', 'tie', 'undershorts', 'pants',
                                                         'belt', 'jacket', 'shoes'])

