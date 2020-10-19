from BSTree import BSTree, BSTreeNode

#first solution is based on the assumption that each node has a link to their parents!

def common_ancestor(node1, node2):
    if node1 is None or node2 is None:
        return None
    node1_ancestor_ptr = node1.parent
    node2_ancestor_ptr = node2.parent
    node1_ancestor_ptr, node2_ancestor_ptr = make_depth_equal(node1_ancestor_ptr, node2_ancestor_ptr)
    while node1_ancestor_ptr is not None and node2_ancestor_ptr is not None:
        if node1_ancestor_ptr == node2_ancestor_ptr:
            return node1_ancestor_ptr
        node1_ancestor_ptr = node1_ancestor_ptr.parent
        node2_ancestor_ptr = node2_ancestor_ptr.parent
    return None


def make_depth_equal(ptr1, ptr2):
    if ptr1 is None or ptr2 is None:
        return
    depth1 = depth(ptr1)
    depth2 = depth(ptr2)
    while depth1 != depth2:
        if depth1 > depth2:
            ptr1 = ptr1.parent
            depth1 -= 1
        else:
            ptr2 = ptr2.parent
            depth2 -= 1
    return ptr1, ptr2


def depth(node):
    if node.parent is None:
        return 0
    return 1 + depth(node.parent)



# second solution; no assumption on the link to each node's parent

def most_common_ancestor2(root, node1, node2):
    if node1 is None or node2 is None or root is None:
        return False, None
    if root == node1 or root == node2:
        return True, None
    left_contains, left_result_node = most_common_ancestor2(root.left, node1, node2)
    right_contains, right_result_node = most_common_ancestor2(root.right, node1, node2)
    if left_result_node is not None:
        return True, left_result_node
    if right_result_node is not None:
        return True, right_result_node
    if left_contains and right_contains:
        return True, root.data
    if left_contains or right_contains:
        return True, None
    else:
        return False, None




tree = BSTree()
tree.insert_key(7)
tree.insert_key(5)
tree.insert_key(2)
tree.insert_key(6)
tree.insert_key(3)
tree.insert_key(1)
tree.insert_key(4)
tree.insert_key(5.5)
result = common_ancestor(tree.search(4), tree.search(5.5))
print(result.data)
print(most_common_ancestor2(tree._root, tree.search(4), tree.search(5.5)))


