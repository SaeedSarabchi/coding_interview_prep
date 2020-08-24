from Stack import Stack


class QueueViaStack:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, data):
        self.enqueue_stack.push(data)

    def dequeue(self):
        if not self.dequeue_stack.is_empty():
            return self.dequeue_stack.pop()
        else:
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()

    def is_empty(self):
        return self.dequeue_stack.is_empty() and self.enqueue_stack.is_emtpy()

    def peek(self):
        top_element = self.dequeue()
        self.dequeue_stack.push(top_element)
        return top_element


my_queue = QueueViaStack()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(my_queue.dequeue())
print(my_queue.dequeue())

my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())