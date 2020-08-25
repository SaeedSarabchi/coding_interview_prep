class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._first = None
        self._last = None

    def is_empty(self):
        return self._first is None

    def add(self, new_data):
        new_node = QueueNode(new_data)
        if self.is_empty():
            self._first = new_node
            self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node

    def peek(self):
        if self.is_empty():
            raise Exception("peeking from an empty queue.")
        else:
            return self._first.data

    def remove(self):
        if self.is_empty():
            raise Exception("removing from an empty queue.")
        else:
            output = self._first.data
            self._first = self._first.next
            if self._first is None:
                self._last = None
            return output

    @property
    def data(self):
        data_list = []
        ptr = self._first
        while ptr is not None:
            data_list.append(ptr.data)
            ptr = ptr.next
        return data_list

    @property
    def first(self):
        return self._first.data

    @first.setter
    def first(self, new_first):
        self._first = new_first

    @property
    def last(self):
        return self.last.data

    @last.setter
    def last(self, new_last):
        self._last = new_last
