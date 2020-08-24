- move all elements less than x to the beginning of the linkedlist. O(N)

def partition(linkedlist, k):
    ptr = linkedlist._head 1
    while ptr.next is not None:
        if ptr.next.data.key < k:
            temp = ptr.next
            ptr.next = ptr.next.next
            temp.next = linkedlist._head
            linkedlist._head = temp
        ptr = ptr.next


init_list = [(1, "val4"), (2, "val3"), (3, "val2"), (4, "val1")]
lili = LinkedList.from_list(init_list)
print(lili.forward)
partition(lili, 2)
print(lili.forward)
