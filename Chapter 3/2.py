class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.min_next = None
        self.a = 1



class Stack2:
    def __init__(self):
        self._top = None
        self._min = None

    def is_empty(self):
        return self._top is None

    def push(self, new_data):
        new_node = StackNode(new_data)
        new_node.next = self._top
        self._top = new_node

        #updating min:
        if self._min is None:
            self._min = new_node
        else:
            if new_data < self._min.data:
                new_node.min_next = self._min
                self._min = new_node

    def peek(self):
        if self.is_empty():
            raise Exception("peeking from an empty stack.")
        return self._top.data

    def pop(self):
        if self.is_empty():
            raise Exception("popping from an empty stack.")
        #updating min:
        if self._min == self._top:
            self._min = self._top.min_next

        output = self._top.data
        self._top = self._top.next
        return output

    def min(self):
        if self.is_empty():
            raise Exception("the stack is empty")
        return self._min.data
    
    
from Stack import Stack


class StackWithMinStack(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()
        
    def push(self, data):
        if super().is_empty():
            self.min_stack.push(data)
        else:
            if data < self.min_stack.peek():
                self.min_stack.push(data)
        super().push(data)

    def pop(self):
        if self.min_stack.peek() == super().top:
            self.min_stack.pop()
        super().pop()

    def min(self):
        return self.min_stack.peek()


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
        



stack = StackWithMinStack()
stack.push(6)
print(stack.min())
stack.push(4)
print(stack.min())
stack.push(5)
print(stack.min())
stack.push(3)
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())
stack.pop()
print(stack.min())