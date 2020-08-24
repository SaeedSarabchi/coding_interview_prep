from LinkedList import *

def remove_duplicates(input_linkedlist):
    reference = input_linkedlist._head
    seen_values = set()
    while reference is not None:
        if (reference.data.key, reference.data.value) in seen_values:
            if reference.prev is not None:
                reference.prev.next = reference.next
            else:
                input_linkedlist._head = reference.next
            if reference.next is not None:
                reference.next.prev = reference.prev
        else:
            seen_values.add((reference.data.key, reference.data.value))
        reference = reference.next

init_list = [(3, "val3"), (2, "val2"), (2, "val2"), (3, "val3")]
ll = LinkedList.from_list(init_list)
remove_duplicates(ll)
print(ll.to_list_forward())