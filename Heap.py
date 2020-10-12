class Heap:
    def __init__(self, array):
        self._array = array
        # self.build_heap()

    def build_heap(self, is_max_heap = True):
        for i in range(len(self._array) // 2, -1, -1):
            self.heapify(i, is_max_heap)

    def heapify(self, i, is_max_heap=True):
        top_element_index = i
        if is_max_heap == True:
            if Heap.left(i) < len(self._array) and self._array[Heap.left(i)] > self._array[top_element_index]:
                top_element_index = Heap.left(i)
            if Heap.right(i) < len(self._array) and self._array[Heap.right(i)] > self._array[top_element_index]:
                top_element_index = Heap.right(i)
        else: #if min_heap
            if Heap.left(i) < len(self._array) and self._array[Heap.left(i)] < self._array[top_element_index]:
                top_element_index = Heap.left(i)
            if Heap.right(i) < len(self._array) and self._array[Heap.right(i)] < self._array[top_element_index]:
                top_element_index = Heap.right(i)
        if top_element_index != i:
            self.swap_array_elements(top_element_index, i)
            self.heapify(top_element_index, is_max_heap)

    def left(i):
        return 2*i + 1

    def right(i):
        return 2*i + 2

    def parent(i):
        return (i-1)//2

    def insert(self, key, is_max_heap=True):
        self._array.append(key)
        index = len(self._array) - 1
        while Heap.parent(index) >= 0 and \
                ((self._array[Heap.parent(index)] < self._array[index] and is_max_heap==True) or \
                 (self._array[Heap.parent(index)] > self._array[index] and is_max_heap==False)):
            self.swap_array_elements(index, Heap.parent(index))
            index = Heap.parent(index)

    def swap_array_elements(self, a, b):
        self._array[a], self._array[b] = self._array[b], self._array[a]

    def extract_top(self,is_max_heap=True):
        self.swap_array_elements(0,len(self._array)-1)
        top = self._array[-1]
        self._array = self._array[:-1]
        self.heapify(0, is_max_heap)
        return top

    def heap_sort(self, is_max_heap=True):
        sorted_list = []
        while len(self._array)>0:
            sorted_list.append(self.extract_top(is_max_heap))
        return sorted_list

