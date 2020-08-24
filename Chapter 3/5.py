from Stack import Stack

def sort_stack(s1):
    s2 = Stack()

    while not s1.is_empty():
        push_largest_from_s1_to_s2(s1, s2)

    print(s2.data)


def push_largest_from_s1_to_s2(s1, s2):
    temp = s1.pop()
    s1_size = 1
    while not s1.is_empty():
        if s1.peek() > temp:
            s2.push(s1.pop())
        else:
            s2.push(temp)
            temp = s1.pop()
        s1_size += 1

    s2.push(temp)
    for i in range(s1_size - 1):
        s1.push(s2.pop())

s1 = Stack()
s1.push(3)
s1.push(4)
s1.push(2)
s1.push(10)
s1.push(3)
s1.push(11)
s1.push(12)
s1.push(1)
sort_stack(s1)
