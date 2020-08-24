from LinkedList import *
class test1:
    def __init__(self):
        self.__list2 = [None]*20

    def __get__(self, instance, owner):
        return self.__list2


    @property
    def list(self):
        print("running getter")
        return self.__list

    @list.setter
    def list(self, value):
        print("running setter")
        self.__list = value

t = test1()
#print(t)

d= "salam"
a = bytearray(d.encode())
#print(a[:2].decode())
#print(a.decode())
#d.append()
#print(d)
matrix = [[None for i in range(2)] for j in range(2)]
matrix[1][0] = 1

#print(matrix)

init_list = [(3, "val3"), (2, "val2"), (1, "val1")]
test = LinkedList.from_list(init_list)
s = set()
print(test._head.data.value)
s.add((test._head.data.key, test._head.data.value))
print(s)
print((1,"val1") in s)


def f(i):
    i[0] = 2

l = [[1],[1],[1]]
f(l[1])
# print(l)

#a=12345678912345678942313213213546546497898654654123456789123456789423132132135465464978986546541234567891234567894231321321354654649789865465412345678912345678942313213213546546497898654654123456789123456789423132132135465464978986546541234567891234567894231321321354654649789865465412345678912345678942313213213546546497898654654123456789123456789423132132135465464978986546541234567891234567894231321321354654649789865465412345678912345678942313213213546546497898654654
import sys
#print(type(a))
#b=12345678912345678942313213213546546497898654654123456789123456789423132132135465464978986546541234567891234567894231321321354654649789865465412345678912345678942313213213546546497898654654123456789123456789423132132135465464978986546541234567891234567894231321321354654649789865465412345678912345678942313213213546546497898654654123456789123456789423132132135465464978986546541234567891234567894231321321354654649789865465412345678912345678942313213213546546497898654654
#print(a+b)
def sample_linkedlist_function():
    linked_list = LinkedList()
    init_linkedlist(linked_list)
    print(linked_list.to_list_forward())
    print(linked_list._head.data.value)
    print(type(linked_list._head))
    return  recursive_linkedlist_to_list_forward(linked_list._head)
    #return iterative_linkedlist_to_list_forward(linked_list._head)


def init_linkedlist(linked_list):
    linked_list.add_node(Node(KeyValue(1,"1")))
    linked_list.add_node(Node(KeyValue(2, "2")))
    linked_list.add_node(Node(KeyValue(3, "3")))


def recursive_linkedlist_to_list_forward(node):
    if node is None:
        return []
    previous_list = recursive_linkedlist_to_list_forward(node.next)
    return [node.data.value] + previous_list


from Stack import Stack
def iterative_linkedlist_to_list_forward(node):
    stack = Stack()
    output = None
    current_data = node
    while True:
        if current_data is None: #base case:
            output = []
            break
        stack.push(current_data)
        current_data = current_data.next
    while not stack.is_empty():
        current_data = stack.pop()
        # recursive part:
        output =  [current_data.data.value] + output
    return output



#print(sample_linkedlist_function())
print("salam")

