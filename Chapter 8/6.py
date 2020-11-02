class Stack:
    def __init__(self):
        self.array = []
    def push(self, data):
        self.array.insert(0,data)
    def pop(self):
        return_element = self.array[0]
        self.array = self.array [1:]
        return return_element

def hanoi(n, src, dst, aux):
    if n == 1:
        move(src, dst)
    else:
        hanoi(n-1, src, aux, dst)
        move(src, dst)
        hanoi(n-1, aux, dst, src)

def move(src, dst):
    print("move")
    dst.push(src.pop())

src = Stack()
src.array = [1,2,3,4,5]
dst = Stack()
aux  = Stack()
hanoi(len(src.array), src, dst, aux)
print(dst.array)
