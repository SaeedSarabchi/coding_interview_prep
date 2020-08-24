from LinkedList import *


def sum_lists(list1, list2):
    list3 = LinkedList()
    ptr1 = list1._head
    ptr2 = list2._head
    carry_over = 0
    while ptr1 is not None or ptr2 is not None:
        num1 = 0
        num2 = 0
        if ptr1 is not None:
            num1 = ptr1.data.key
            ptr1 = ptr1.next
        if ptr2 is not None:
            num2 = ptr2.data.key
            ptr2 = ptr2.next
        digit = (num1 + num2 + carry_over) % 10
        carry_over = (num1 + num2 + carry_over) // 10
        new_node = Node(KeyValue(digit, str(digit)))
        list3.add_node(new_node)
    if carry_over == 1:
        new_node = Node(KeyValue(1, str(1)))
        list3.add_node(new_node)
    return list3


init_list = []
list1 = LinkedList.from_list(init_list)
init_list = [(9, "9"), (5, "5"), (3, "3"), (9, "9")]
list2 = LinkedList.from_list(init_list)
res = sum_lists(list1, list2)
print(res.to_list_forward())

def reverse_list(input_list):
    ptr = input_list._head
    if ptr is None:
        return
    while ptr.next is not None:
        temp = ptr.next
        if ptr.next is not None:
            ptr.next = ptr.next.next
        temp.next = input_list._head
        input_list._head = temp

init_list = [(9, "9"), (5, "5"), (3, "3"), (8, "8")]
list1 = LinkedList.from_list(init_list)
print(list1.to_list_forward())

reverse_list(list1)
print(list1.to_list_forward())