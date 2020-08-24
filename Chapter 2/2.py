from LinkedList import *
def return_k_th_to_last(input_linkedlist, k):
    counter_ptr = input_linkedlist._head
    node_ptr = input_linkedlist._head
    element_count = 0
    while counter_ptr is not None:
        element_count += 1
        counter_ptr = counter_ptr.next
    if k > element_count:
        return "k larger than element count"
    for i in range(element_count - k):
        node_ptr = node_ptr.next
    return node_ptr.data.key

init_list = [(4, "val3"), (3, "val2"), (2, "val2"), (1, "val1")]
lili = LinkedList.from_list(init_list)
print(return_k_th_to_last(lili, 2))

init_list = [(1, "val1")]
lili = LinkedList.from_list(init_list)
print(return_k_th_to_last(lili, 1))

init_list = []
lili = LinkedList.from_list(init_list)
print(return_k_th_to_last(lili, 2))


def count_linkedlist_recursively(input_linkedlist, k):
    if input_linkedlist is None:
        return 0, None
    else:
        last_k_count,result =  count_linkedlist_recursively(input_linkedlist.next, k)
        if 1+last_k_count == k:
            return 1+last_k_count, input_linkedlist.data.key
        else:
            return 1+last_k_count, result

init_list = [(4, "val3"), (3, "val2"), (2, "val2"), (1, "val1")]
lili = LinkedList.from_list(init_list)
print(count_linkedlist_recursively(lili._head, 2))


