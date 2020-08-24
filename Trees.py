class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self, root):
        self.root = root

    def print_pre_order(self, tree_node):
        print(tree_node.data)
        for child in tree_node.children:
            self.print_pre_order(child)

    def print_post_order(self, tree_node):
        for child in tree_node.children:
            self.print_pre_order(child)
        print(tree_node.data)


root_node = TreeNode("root")
tree = Tree(root_node)
child1 = TreeNode("child1")
tree.root.children.append(child1)
child2 = TreeNode("child2")
tree.root.children.append(child2)
grand_child1_1 = TreeNode("grand_child1_1")
tree.root.children[0].children.append(grand_child1_1)
grand_child2_1 = TreeNode("grand_child2_1")
tree.root.children[1].children.append(grand_child2_1)
tree.print_post_order(tree.root)