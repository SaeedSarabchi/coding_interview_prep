import unittest
from BSTree import BSTree


class TestBSTree(unittest.TestCase):
    def init_tree(self):
        self.tree = BSTree()
        self.tree.insert_key(1)
        self.tree.insert_key(5)
        self.tree.insert_key(3)
        self.tree.insert_key(2)
        self.tree.insert_key(3.4)

    def test_insert(self):
        self.init_tree()
        self.assertEqual(self.tree.in_order(), [1, 2, 3, 3.4, 5])

    def test_pre_order(self):
        self.init_tree()
        self.assertEqual(self.tree.pre_order(), [1,5,3,2,3.4])

    def test_post_order(self):
        self.init_tree()
        self.assertEqual(self.tree.post_order(), [2,3.4,3,5,1])

    def test_search(self):
        self.init_tree()
        self.assertEqual(self.tree.search(3), self.tree.root.right.left)

    def test_min(self):
        self.init_tree()
        self.assertEqual(self.tree.min(), self.tree.root)

    def test_max(self):
        self.init_tree()
        self.assertEqual(self.tree.max(), self.tree.root.right)

    def test_successor_with_right(self):
        self.init_tree()
        self.assertEqual(self.tree.root.successor(), self.tree.root.right.left.left, "has right")

    def test_successor_without_right(self):
        self.tree = BSTree()
        self.tree.insert_key(6)
        self.tree.insert_key(7)
        self.tree.insert_key(1)
        self.tree.insert_key(5)
        self.tree.insert_key(3)
        self.tree.insert_key(2)
        self.tree.insert_key(3.4)
        self.assertEqual(self.tree.root.left.right.successor(), self.tree.root, "does not have right")

    def test_predecessor_with_left(self):
        self.init_tree()
        self.assertEqual(self.tree.root.right.predecessor(), self.tree.root.right.left.right, "has left")

    def test_predecessor_without_left(self):
        self.tree = BSTree()
        self.tree.insert_key(0)
        self.tree.insert_key(6)
        self.tree.insert_key(1)
        self.tree.insert_key(5)
        self.tree.insert_key(3)
        self.tree.insert_key(2)
        self.tree.insert_key(3.4)
        self.assertEqual(self.tree.root.right.left.predecessor(), self.tree.root, "does not have left")

    def test_delete_no_child(self):
        self.init_tree()
        self.tree.delete(self.tree.root.right.left.left)
        self.assertEqual(self.tree.in_order(), [1,3,3.4,5])

    def test_delete_one_child(self):
        self.init_tree()
        self.tree.delete(self.tree.root.right)
        self.assertEqual(self.tree.in_order(), [1,2,3,3.4])
        self.tree.delete(self.tree.root)
        self.assertEqual(self.tree.in_order(), [2, 3, 3.4])

    def test_delete_two_children_successor_right(self):
        self.init_tree()
        self.tree.insert_key(1.5)
        self.tree.insert_key(2.5)
        self.tree.insert_key(4)
        self.tree.insert_key(3.5)
        self.tree.insert_key(4.5)
        self.tree.delete(self.tree.search(3))
        self.assertEqual(self.tree.in_order(), [1,1.5,2,2.5,3.4,3.5,4,4.5,5])

    def test_delete_two_children_successor_not_right(self):
        self.init_tree()
        self.tree.insert_key(1.5)
        self.tree.insert_key(2.5)
        self.tree.insert_key(4)
        self.tree.insert_key(3.5)
        self.tree.insert_key(4.5)
        self.tree.insert_key(3.2)
        self.tree.insert_key(3.3)
        self.tree.delete(self.tree.search(3))
        self.assertEqual(self.tree.in_order(), [1,1.5,2,2.5,3.2,3.3,3.4,3.5,4,4.5,5])