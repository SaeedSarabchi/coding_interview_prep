from BSTree import BSTreeNode, BSTree


class AVLTreeNode(BSTreeNode):
    def __init__(self, data):
        BSTreeNode.__init__(self, data)
        self.height = 0

    def insert_key(self, input_node):
        BSTreeNode.insert_key(self, input_node)
        if input_node.parent is not None:
            input_node.parent.update_heights_upward()

    @property
    def right_height(self):
        right_child_height = -1
        if self.right is not None:
            right_child_height = self.right.height
        return right_child_height

    @right_height.setter
    def right_height(self, height):
        self.right.height = height

    @property
    def left_height(self):
        left_child_height = -1
        if self.left is not None:
            left_child_height = self.left.height
        return left_child_height

    @left_height.setter
    def left_height(self, height):
        self.left.height = height

    def update_heights_upward(self):
        max_left_right = max(self.left_height, self.right_height)
        if self.height <= max_left_right:
            self.height = 1 + max_left_right
            if self.parent is not None:
                self.parent.update_heights_upward()


class AVLTree(BSTree):
    def insert_key(self, input_data):
        new_node = AVLTreeNode(input_data)
        if self._root is not None:
            self._root.insert_key(new_node)
            self.balance_upwards(new_node.parent)
        else:
            self._root = new_node

    def balance_upwards(self, node):
        if abs(node.left_height - node.right_height) >= 2:
            self.rotate(node)
        if abs(node.left_height - node.right_height) >= 1:
            if node.parent is not None:
                self.balance_upwards(node.parent)

    def rotate(self, node):
        if node.left_height > node.right_height:
            if node.left.right_height > node.left.left_height:
                self.rotate_left(node.left)
            self.rotate_right(node)
        else:
            if node.right.left_height > node.right.right_height:
                self.rotate_right(node.right)
            self.rotate_left(node)

    def rotate_right(self, node):
        buffered_node_left = node.left
        #update node's parent
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = buffered_node_left
                buffered_node_left.parent = node.parent.left
            else:
                node.parent.right = buffered_node_left
                buffered_node_left.parent = node.parent.right
        else: #node is root
            self._root = buffered_node_left
            buffered_node_left.parent = None
        node.left = buffered_node_left.right
        if buffered_node_left.right is not None:
            buffered_node_left.right.parent = node
        buffered_node_left.right = node
        node.parent = buffered_node_left

    def rotate_left(self, node):
        buffered_node_right = node.right
        #update node's parent
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = buffered_node_right
                buffered_node_right.parent = node.parent.left
            else:
                node.parent.right = buffered_node_right
                buffered_node_right.parent = node.parent.right
        else: #node is root
            self._root = buffered_node_right
            buffered_node_right.parent = None
        node.right = buffered_node_right.left
        if buffered_node_right.left is not None:
            buffered_node_right.left.parent = node
        buffered_node_right.left = node
        node.parent = buffered_node_right

    def _transplant(self, to_be_deleted, to_be_substituted):
        to_be_deleted_parent = to_be_deleted.parent
        BSTree._transplant(self, to_be_deleted, to_be_substituted)
        if to_be_deleted_parent is not None:
            to_be_deleted_parent.update_heights_upward()
            self.balance_upwards(to_be_deleted_parent)