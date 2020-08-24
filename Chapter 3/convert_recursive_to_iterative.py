from LinkedList import *
from Stack import Stack


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


print(sample_linkedlist_function())