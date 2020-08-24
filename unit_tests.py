import unittest
from LinkedList import LinkedList, Node, KeyValue
from ArrayList import ArrayList
from StringBuilder import StringBuilder
from HashTable import HashTable
from Stack import Stack
from Queue import Queue


class TestLinkList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def init_linked_list(self):
        node_3 = Node(KeyValue(3, "val3"))
        self.linked_list.add_node(node_3)
        node_2 = Node(KeyValue(2, "val2"))
        self.linked_list.add_node(node_2)
        node_1 = Node(KeyValue(1, "val1"))
        self.linked_list.add_node(node_1)

    def test_to_list_forward(self):
        self.init_linked_list()
        self.assertEqual(self.linked_list.to_list_forward(), [(1,"val1"),(2,"val2"),(3,"val3")])

    def test_to_list_backward(self):
        self.init_linked_list()
        self.assertEqual(self.linked_list.to_list_backward(), [(3, "val3"), (2, "val2"), (1, "val1")])

    def test_sanity_check(self):
        self.init_linked_list()
        self.assertEqual(self.linked_list.sanity_check(), True)

    def test_get_first_node(self):
        self.init_linked_list()
        first_node = self.linked_list.get_first_node()
        self.assertEqual(first_node.data.key, 1)
        self.assertEqual(first_node.data.value, "val1")

    def test_get_last_node(self):
        self.init_linked_list()
        last_node = self.linked_list.get_last_node()
        self.assertEqual(last_node.data.key, 3)
        self.assertEqual(last_node.data.value, "val3")

    def test_add_multiple(self):
        node_3 = Node(KeyValue(3, "val3"))
        self.linked_list.add_node(node_3)
        self.assertEqual(self.linked_list.to_list_forward(), [(3,"val3")])
        self.assertEqual(self.linked_list.sanity_check(), True)
        node_2 = Node(KeyValue(2, "val2"))
        self.linked_list.add_node(node_2)
        self.assertEqual(self.linked_list.to_list_forward(), [(2, "val2"),(3,"val3")])
        self.assertEqual(self.linked_list.sanity_check(), True)
        node_1 = Node(KeyValue(1, "val1"))
        self.linked_list.add_node(node_1)
        self.assertEqual(self.linked_list.to_list_forward(), [(1, "val1"),(2,"val2"),(3,"val3")])
        self.assertEqual(self.linked_list.sanity_check(), True)

    def test_find(self):
        self.init_linked_list()
        node_3 = self.linked_list.find_node_by_key(3)
        self.assertEqual(node_3.data.key, 3)
        self.assertRaises(KeyError, lambda:self.linked_list.find_node_by_key(101))

    def test_delete(self):
        self.init_linked_list()
        self.linked_list.delete_node_by_key(2)
        self.assertRaises(KeyError, lambda:self.linked_list.find_node_by_key(2))
        self.assertRaises(KeyError, lambda: self.linked_list.delete_node_by_key(2))
        self.assertEqual(self.linked_list.to_list_forward(), [(1, "val1"), (3, "val3")])
        self.assertEqual(self.linked_list.sanity_check(), True)
        self.linked_list.delete_node_by_key(3)
        self.assertRaises(Exception, lambda: self.linked_list.find_node_by_key(3))
        self.assertEqual(self.linked_list.to_list_forward(), [(1, "val1")])
        self.assertEqual(self.linked_list.sanity_check(), True)
        self.linked_list.delete_node_by_key(1)
        self.assertRaises(KeyError, lambda: self.linked_list.find_node_by_key(1))
        self.assertEqual(self.linked_list.to_list_forward(), [])
        self.assertEqual(self.linked_list.sanity_check(), True)
        self.assertRaises(KeyError, lambda: self.linked_list.delete_node_by_key(1))

    def test_len(self):
        self.init_linked_list()
        self.assertEqual(len(self.linked_list), 3)

    def test_init_from_list(self):
        init_list = [(3, "val3"), (2, "val2"), (1, "val1")]
        self.linked_list = LinkedList.from_list(init_list)
        self.assertEqual(self.linked_list.to_list_forward(), [(1, "val1"), (2, "val2"), (3, "val3")])


class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.ARRAY_LIST_INIT_SIZE = 2
        self.array_list = ArrayList(self.ARRAY_LIST_INIT_SIZE)

    def array_list_sanity_check(self, orig_len, orig_list, number_of_elements):
        self.assertEqual(self.array_list.orig_len, orig_len)
        self.assertEqual(self.array_list.orig_list, orig_list)
        self.assertEqual(len(self.array_list), number_of_elements)

    def test_initialization(self):
        self.array_list_sanity_check(2, [None]*self.ARRAY_LIST_INIT_SIZE, 0)

    def test_append(self):
        self.array_list.append(1)
        self.array_list_sanity_check(2, [1, None], 1)
        self.array_list.append(2)
        self.array_list_sanity_check(2, [1,2], 2)
        self.array_list.append(3)
        self.array_list_sanity_check(4, [1, 2, 3, None], 3)
        self.array_list.append(4)
        self.array_list_sanity_check(4, [1, 2, 3, 4], 4)


class TestStringBuilder(unittest.TestCase):
    def setUp(self):
        StringBuilder._INIT_SIZE = 2
        self.string_builder = StringBuilder()

    def string_builder_sanity_check(self, orig_list, number_of_elements):
        self.assertEqual(self.string_builder.orig_list, orig_list)
        self.assertEqual(len(self.string_builder), number_of_elements)

    def test_initialization(self):
        self.string_builder_sanity_check([None]*StringBuilder._INIT_SIZE, 0)

    def test_append(self):
        self.string_builder.append("a")
        self.string_builder_sanity_check(['a', None], 1)
        self.string_builder.append("b")
        self.string_builder_sanity_check(['a','b'], 2)
        self.string_builder.append("c")
        self.string_builder_sanity_check(['a', 'b', 'c', None], 3)
        self.string_builder.append("de")
        self.string_builder_sanity_check(['a', 'b', 'c', 'd', 'e', None, None, None], 5)


class TestHashTable(unittest.TestCase):
    def setUp(self):
        HashTable._INIT_SIZE = 2
        self.hash_table = HashTable()

    def test_init(self):
        self.assertEqual(self.hash_table.hash_to_list(), [None, None])

    def test_put_no_rehashing(self):
        self.hash_table[1]="1"
        self.assertEqual(self.hash_table.hash_to_list(), [None, [(1,"1")]])
        self.hash_table[2] = "2"
        self.assertEqual(self.hash_table.hash_to_list(), [[(2,"2")], [(1, "1")]])

    def test_put_rehashing(self):
        self.hash_table[1] = "1"
        self.hash_table[2] = "2"
        self.hash_table[3] = "3"
        self.assertEqual(self.hash_table.hash_to_list(), [None, [(1,"1")], [(2,"2")], [(3,"3")]])

    def test_put_chaining(self):
        self.hash_table[1] = "1"
        self.hash_table[2] = "2"
        self.hash_table[3] = "3"
        self.hash_table[6] = "6"
        self.assertEqual(self.hash_table.hash_to_list(), [None, [(1, "1")], [(6, "6"), (2,"2")], [(3, "3")]])

    def test_delete(self):
        self.hash_table[1] = "1"
        self.hash_table[2] = "2"
        self.hash_table[3] = "3"
        self.hash_table[6] = "6"
        del self.hash_table[2]
        self.assertEqual(self.hash_table.hash_to_list(), [None, [(1, "1")], [(6, "6")], [(3, "3")]])
        del self.hash_table[3]
        self.assertEqual(self.hash_table.hash_to_list(), [None, [(1, "1")], [(6, "6")], None])

    def test_raise_key_error(self):
        self.assertRaises(KeyError, lambda:self.hash_table[2])
        self.hash_table[2] = "2"
        self.assertRaises(KeyError, lambda: self.hash_table[3])


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def stack_push_small(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

    def sanity_check(self, input_data):
        self.assertEqual(self.stack.data, input_data)

    def test_init(self):
        self.sanity_check([])

    def test_push(self):
        self.stack.push("hi")
        self.sanity_check(["hi"])
        self.stack.push("hello")
        self.sanity_check(["hello", "hi"])

    def test_peek(self):
        self.stack_push_small()
        self.assertEqual(self.stack.peek(), 3)

    def test_pop(self):
        self.stack_push_small()
        output = self.stack.pop()
        self.assertEqual(output, 3)
        self.sanity_check([2, 1])
        output = self.stack.pop()
        self.assertEqual(output, 2)
        self.sanity_check([1])
        output = self.stack.pop()
        self.assertEqual(output, 1)
        self.sanity_check([])

    def test_peek_error(self):
        self.assertRaises(Exception, lambda:self.stack.peek())

    def test_pop_error(self):
        self.assertRaises(Exception, lambda: self.stack.pop())


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def queue_add_small(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.add(3)

    def sanity_check(self, input_data):
        self.assertEqual(self.queue.data, input_data)

    def test_init(self):
        self.sanity_check([])

    def test_add(self):
        self.queue.add("hi")
        self.sanity_check(["hi"])
        self.queue.add("hello")
        self.sanity_check(["hi", "hello"])

    def test_peek(self):
        self.queue_add_small()
        self.assertEqual(self.queue.peek(), 1)

    def test_remove(self):
        self.queue_add_small()
        output = self.queue.remove()
        self.assertEqual(output, 1)
        self.sanity_check([2, 3])
        output = self.queue.remove()
        self.assertEqual(output, 2)
        self.sanity_check([3])
        output = self.queue.remove()
        self.assertEqual(output, 3)
        self.sanity_check([])

    def test_peek_error(self):
        self.assertRaises(Exception, lambda:self.queue.peek())

    def test_pop_error(self):
        self.assertRaises(Exception, lambda: self.queue.remove())

if __name__ == '__main__':
    unittest.main()
