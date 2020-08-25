class Heap:
    def __init__(self, array):
        self._array = array
        # self.build_heap()

    def build_heap(self):
        for i in range(len(self._array) // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_element_index = i
        if Heap.left(i) < len(self._array) and self._array[Heap.left(i)] > self._array[largest_element_index]:
            largest_element_index = Heap.left(i)
        if Heap.right(i) < len(self._array) and self._array[Heap.right(i)] > self._array[largest_element_index]:
            largest_element_index = Heap.right(i)
        if largest_element_index != i:
            self.swap_array_elements(largest_element_index, i)
            self.heapify(largest_element_index)

    def left(i):
        return 2*i + 1

    def right(i):
        return 2*i + 2

    def parent(i):
        return (i-1)//2

    def insert(self, key):
        self._array.append(key)
        index = len(self._array) - 1
        while Heap.parent(index) >= 0 and self._array[Heap.parent(index)] < self._array[index]:
            self.swap_array_elements(index, Heap.parent(index))
            index = Heap.parent(index)

    def swap_array_elements(self, a, b):
        self._array[a], self._array[b] = self._array[b], self._array[a]

    def extract_max(self):
        self.swap_array_elements(0,len(self._array)-1)
        max = self._array[-1]
        self._array = self._array[:-1]
        self.heapify(0)
        return max

    def heap_sort(self):
        sorted_list = []
        while len(self._array)>0:
            sorted_list.append(self.extract_max())
        return sorted_list

