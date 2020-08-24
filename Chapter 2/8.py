from LinkedList import *
#import LinkedList


def find_loop_node(input_list):
    if input_list._head is None:
        return None

    slow = input_list._head
    fast = input_list._head

    is_looped = False
    first = True

    while slow.next is not None and fast.next is not None and fast.next.next is not None: #  slow.next is not None This is !!excessive!!
        if slow == fast:
            if first:
                first = False
            else:
                is_looped = True
                break
        slow = slow.next
        fast = fast.next.next

    if not is_looped:
        return None

    ptr = input_list._head
    while ptr != slow:
        ptr = ptr.next
        slow = slow.next
    return (ptr.data.key, ptr.data.value)



init_list = [(1, "k"), (2, "a"),(2.5, "y"),(2.6, "y"),(2.7, "z"), (3, "a"), (4, "k")]
list1 = LinkedList.from_list(init_list)
list1._head.next.next.next.next.next.next.next  = list1._head.next.next
print(find_loop_node(list1))
