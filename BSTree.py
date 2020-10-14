class BSTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert_key(self, input_node):
        if input_node.data <= self.data:
            if self.left is None:
                self.left = input_node
                self.left.parent = self
                #return self.left
            else:
                self.left.insert_key(input_node)
        else:
            if self.right is None:
                self.right = input_node
                self.right.parent = self
                #return self.right
            else:
                self.right.insert_key(input_node)

    def in_order(self):
        left = []
        if self.left is not None:
            left = self.left.in_order()
        right = []
        if self.right is not None:
            right = self.right.in_order()
        return left + [self.data] + right

    def pre_order(self):
        left = []
        if self.left is not None:
            left = self.left.pre_order()
        right = []
        if self.right is not None:
            right = self.right.pre_order()
        return [self.data] + left + right

    def post_order(self):
        left = []
        if self.left is not None:
            left = self.left.post_order()
        right = []
        if self.right is not None:
            right = self.right.post_order()
        return left + right + [self.data]

    def search(self, data):
        if self.data != data:
            if data <= self.data:
                if self.left is not None:
                    return self.left.search(data)
                else:
                    return None
            else:
                if self.right is not None:
                    return self.right.search(data)
                else:
                    return None
        else:
            return self

    def min(self):
        if self.left is None:
            return self
        else:
            return self.left.min()

    def max(self):
        if self.right is None:
            return self
        else:
            return self.right.max()

    def successor(self):
        if self.right is not None:
            return self.right.min()
        else:
            current_node = self
            parent = self.parent
            while parent is not None and parent.right == current_node:
                current_node = current_node.parent
                parent = current_node.parent
            return parent

    def predecessor(self):
        if self.left is not None:
            return self.left.max()
        else:
            current_node = self
            parent = self.parent
            while parent is not None and parent.left == current_node:
                current_node = current_node.parent
                parent = current_node.parent
            return parent


class BSTree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert_key(self, input_data):
        new_node = BSTreeNode(input_data)
        if self._root is not None:
            self._root.insert_key(new_node)
        else:
            self._root = new_node

    def in_order(self):
        if self._root is not None:
            return self._root.in_order()
        else:
            return None

    def pre_order(self):
        if self._root is not None:
            return self._root.pre_order()
        else:
            return None

    def post_order(self):
        if self._root is not None:
            return self._root.post_order()
        else:
            return None

    def search(self, data):
        if self._root is not None:
            return self._root.search(data)
        else:
            return None

    def min(self):
        if self._root is not None:
            return self._root.min()
        else:
            return None

    def max(self):
        if self._root is not None:
            return self._root.max()
        else:
            return None

    def delete(self, input_node):
        if input_node.left is None and input_node.right is None:
            self._transplant(input_node, None)
        elif input_node.left is None or input_node.right is None:
            substitute_node = None
            if input_node.left is None:
                substitute_node = input_node.right
            else:
                substitute_node = input_node.left
            self._transplant(input_node, substitute_node)
        else:
            successor = input_node.successor()
            if successor == input_node.right:
                self._transplant(input_node, successor)
                successor.left = input_node.left
                input_node.left.parent = successor
            else:
                input_node.data = successor.data
                self._transplant(successor, successor.right)

    def _transplant(self, to_be_deleted, to_be_substituted):
        if to_be_deleted.parent is not None:
            if to_be_deleted.parent.left == to_be_deleted:
                to_be_deleted.parent.left = to_be_substituted
            else:
                to_be_deleted.parent.right = to_be_substituted
        else:
            self._root = to_be_substituted


