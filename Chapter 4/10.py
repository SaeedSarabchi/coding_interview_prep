from BSTree import BSTree


def is_subtree(tree1, tree2):
    tree2_height = height(tree2._root)

    # for all of tree1's children with height tree2_height, check if the subtree is identical to tree2
    return check_is_subtree(tree1._root, tree2_height, tree2._root)


def check_is_subtree(root, tree2_height, tree2_root):
    if root is None and tree2_root is not None:
        return -1, False
    if root is None and tree2_root is None:
        return -1, True

    left_height, left_found = check_is_subtree(root.left, tree2_height, tree2_root)
    if left_found:
        return -2, True
    right_height, right_found = check_is_subtree(root.right, tree2_height, tree2_root)
    if right_found:
        return -2, True
    height = 1 + max(left_height, right_height)
    if height == tree2_height:
        found = is_identical(root, tree2_root)
        if found:
            return -2, True

    return height, False


def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)


def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


tree1 = BSTree()
tree1.insert_key(2)
tree1.insert_key(1)
tree1.insert_key(3)
tree1.insert_key(2.5)
tree1.insert_key(4)
tree1.insert_key(0.5)
tree1.insert_key(1.5)
tree1.insert_key(2.7)

tree2 = BSTree()
tree2.insert_key(3)
tree2.insert_key(2.5)
tree2.insert_key(4.4)
tree2.insert_key(2.7)

print(is_subtree(tree1, tree2))
