import unittest
from AVLTree import AVLTree


class TestAVLTree(unittest.TestCase):
    def init_tree(self):
        self.tree = AVLTree()
        self.tree.insert_key(1)
        self.tree.insert_key(5)
        self.tree.insert_key(3)
        self.tree.insert_key(2)
        self.tree.insert_key(3.4)

    def test_insert(self):
        self.init_tree()
        self.assertEqual(self.tree.pre_order(), [3,1,2,5,3.4])

    def test_delete(self):
        self.init_tree()
        self.tree.delete(self.tree.root.left.right)
        self.tree.delete(self.tree.root.left)
        self.assertEqual(self.tree.pre_order(), [3.4,3,5])
