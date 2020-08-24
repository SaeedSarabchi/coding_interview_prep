from LinkedList import *

#bug: when you have if ptr.next, and then you actually change the ptr.next, then you shouldn't increment the ptr, hence
# in these cases you should always have 'else'!
def partition(linkedlist, k):
    ptr = linkedlist._head
    while ptr is not None and ptr.next is not None:
        if ptr.next.data.key < k:
            temp = ptr.next
            ptr.next = ptr.next.next
            temp.next = linkedlist._head
            linkedlist._head = temp
        else:
            ptr = ptr.next


init_list = [(1, "val4"), (2, "val3"), (3, "val2"), (4, "val1")]
lili = LinkedList.from_list(init_list)
print(lili.to_list_forward())
partition(lili, 5)
print(lili.to_list_forward())