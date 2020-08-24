class SingleStackWithArray:
    ARRAY_SIZE = 10

    def __init__(self):
        self._data = [None] * SingleStackWithArray.ARRAY_SIZE
        self._top = -1

    def _next_available_index(self):
        return self._top + 1

    def _is_full(self):
        return self._top == SingleStackWithArray.ARRAY_SIZE - 1

    def push(self, item):
        if self._is_full():
            raise Exception("stack full.")
        self._data[self._next_available_index()] = item
        self._top += 1

    def is_empty(self):
        return self._top == -1

    def pop(self):
        if self.is_empty():
            raise Exception("stack empty.")
        output = self._data[self._top]
        self._top -= 1
        return output

stack = SingleStackWithArray()
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
print(stack._top)
print(stack._data)
