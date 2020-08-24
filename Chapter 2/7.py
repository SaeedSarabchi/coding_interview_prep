from LinkedList import *


def list_size(input_list):
    ptr = input_list._head
    size = 0
    while ptr is not None:
        size += 1
        ptr = ptr.next
    return size


def has_intersection(list1, list2):
    shorter = LinkedList()
    longer = LinkedList()
    list1_size = list_size(list1)
    list2_size = list_size(list2)
    if list1_size > list2_size:
        longer = list1
        shorter = list2
    else:
        longer = list2
        shorter = list1

    ptr_shorter = shorter._head
    ptr_longer = longer._head

    difference_in_size = abs(list1_size - list2_size)
    for i in range(difference_in_size):
        ptr_longer = ptr_longer.next

    while ptr_longer is not None:
        if ptr_shorter == ptr_longer:
            return True, str(ptr_shorter.data.value)
        ptr_shorter = ptr_shorter.next
        ptr_longer = ptr_longer.next
    return False, None


init_list = [(1, "k"), (2, "a"),(2.5, "y"),(2.6, "y"),(2.7, "z"), (3, "a"), (4, "k")]
list1 = LinkedList.from_list(init_list)
list2 = LinkedList()
new_node = Node(KeyValue(12,"12"))
list2.add_node(new_node)
new_node = Node(KeyValue(13,"13"))
list2.add_node(new_node)
list2._head.next.next = list1._head
list3 = LinkedList()
new_node = Node(KeyValue(14,"14"))
list3.add_node(new_node)
new_node = Node(KeyValue(15,"15"))
list3.add_node(new_node)
new_node = Node(KeyValue(16,"16"))
list3.add_node(new_node)
new_node = Node(KeyValue(17,"17"))
list3.add_node(new_node)
#list3._head.next.next.next.next = list1._head

print(has_intersection(list3, list2))