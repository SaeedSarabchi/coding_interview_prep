from BSTree import BSTree, BSTreeNode


def validate(tree):
    return is_bst(tree._root, -float("inf"), float("inf"))


def is_bst(node, min_range, max_range):
    #base case
    if node is None:
        return True

    if node.data <= min_range:
        return False

    if node.data > max_range:
        return False

    return is_bst(node.left, min_range, node.data) and is_bst(node.right, node.data, max_range)

tree = BSTree()
tree.insert_key(5)
tree._root.left = BSTreeNode(2)
tree._root.left.right = BSTreeNode(5)
tree._root.right = BSTreeNode(6)
print(validate(tree))