from BSTree import BSTree


def successor(node):
    if node is None:
        return None

    # if the node has a right child
    if node.right is not None:
        return left_most(node.right)
    else:
        node_ptr = node
        while node_ptr.parent is not None:
            if node_ptr.parent.left == node_ptr:
                return node_ptr.parent
            node_ptr = node_ptr.parent
    return None


def left_most(node):
    if node is None:
        return None
    if node.left is None:
        return node
    return left_most(node.left)


tree = BSTree()
tree.insert_key(5)
tree.insert_key(2)
tree.insert_key(6)
tree.insert_key(3)
tree.insert_key(1)
tree.insert_key(4)
tree.insert_key(5.5)
print(successor(tree._root).data)
print(successor(tree._root.left.right.right).data)