class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, new_data):
        new_node = StackNode(new_data)
        new_node.next = self._top
        self._top = new_node

    def peek(self):
        if self.is_empty():
            raise Exception("peeking from an empty stack.")
        return self._top.data

    def pop(self):
        if self.is_empty():
            raise Exception("popping from an empty stack.")
        output = self._top.data
        self._top = self._top.next
        return output

    @property
    def data(self):
        data_list = []
        ptr = self._top
        while ptr is not None:
            data_list.append(ptr.data)
            ptr = ptr.next
        return data_list

    @property
    def top(self):
        return self._top.data

    @top.setter
    def top(self, new_top):
        self._top = new_top
