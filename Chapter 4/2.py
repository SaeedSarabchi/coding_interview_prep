
class BSTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, new_node):
        if new_node.data <= self.data:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(new_node)
        else:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(new_node)


class BSTree:
    def __init__(self):
        self._root = None

    def insert(self, new_node):
        if self._root is None:
            self._root = new_node
        else:
            self._root.insert(new_node)


def build_minimal_bstree_from_sorted_array(sorted_array):
    bstree = BSTree()
    add_mid_array_recursively(bstree, sorted_array, None, None)
    return bstree


def add_mid_array_recursively(bstree, sorted_array, parent, is_left):
    if len(sorted_array) == 0:
        return

    mid_element_idx = len(sorted_array)//2

    mid_element = sorted_array[mid_element_idx]
    new_node = BSTreeNode(mid_element)
    if parent is None:
        bstree._root = new_node
    else:
        if is_left:
            parent.left = new_node
        else:
            parent.right = new_node
    add_mid_array_recursively(bstree, sorted_array[0:mid_element_idx], new_node, True)
    add_mid_array_recursively(bstree, sorted_array[mid_element_idx+1:], new_node, False)


def build_minimal_bstree_from_sorted_array2(sorted_array):
    bstree = BSTree()
    bstree._root = add_mid_array_recursively2(bstree, sorted_array)
    return bstree


def add_mid_array_recursively2(bstree, sorted_array):
    if len(sorted_array) == 0:
        return None

    mid_element_idx = len(sorted_array)//2
    mid_element = sorted_array[mid_element_idx]
    new_node = BSTreeNode(mid_element)
    new_node.left = add_mid_array_recursively2(bstree, sorted_array[0:mid_element_idx])
    new_node.right = add_mid_array_recursively2(bstree, sorted_array[mid_element_idx+1:])
    return new_node


sorted_array = [1,2,3,4,5,6,7]
result_tree = build_minimal_bstree_from_sorted_array2(sorted_array)
print(result_tree)