import unittest
from Heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap([])

    def init_heap(self):
        self.heap = Heap([1, 2, 3, 4, 5])

    def test_heapify(self):
        self.init_heap()
        self.heap.heapify(0)
        self.assertEqual(self.heap._array, [3, 2, 1, 4, 5])

    def test_build_heap1(self):
        self.init_heap()
        self.heap.build_heap()
        self.assertEqual(self.heap._array, [5, 4, 3, 1, 2])

    def test_build_heap2(self):
        self.heap = Heap([1, 2, 3, 4, 5, 6])
        self.heap.build_heap()
        self.assertEqual(self.heap._array, [6, 5, 3, 4, 2, 1])

    def test_insert(self):
        self.init_heap()
        self.heap.build_heap()
        self.heap.insert(6)
        self.assertEqual(self.heap._array, [6, 4, 5, 1, 2, 3])

    def test_extract_max(self):
        self.init_heap()
        self.heap.build_heap()
        self.heap.extract_top()
        self.assertEqual(self.heap._array, [4, 2, 3, 1])

    def test_heap_sort(self):
        self.heap = Heap([1,3,5,6,3,2,1,2,5,6,6,17,19,10])
        self.heap.build_heap()
        self.assertEqual(self.heap.heap_sort(), [19, 17, 10, 6, 6, 6, 5, 5, 3, 3, 2, 2, 1, 1])

    def test_min_heap_sort(self):
        self.heap = Heap([1, 3, 5, 6, 3, 2, 1, 2, 5, 6, 6, 17, 19, 10])
        self.heap.build_heap(False)
        self.assertEqual(self.heap.heap_sort(False), [1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 6, 10, 17, 19])




if __name__ == '__main__':
    unittest.main()
