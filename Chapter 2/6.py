from LinkedList import *


def is_linkedlist_palindrome(input_list):
    size = 0
    ptr = input_list._head
    while ptr is not None:
        size += 1
        ptr = ptr.next

    # reversing the first half of the elements
    running_ptr = input_list._head
    for i in range(size//2-1):
        temp = running_ptr.next
        running_ptr.next = running_ptr.next.next
        temp.next = input_list._head
        input_list._head = temp
    if size%2 == 1:
        running_ptr.next = running_ptr.next.next
    running_ptr = running_ptr.next

    # checking if the list is palindrome
    secondary_ptr = input_list._head
    for i in range(size//2):
        if secondary_ptr.data.value != running_ptr.data.value:
            return False
        secondary_ptr = secondary_ptr.next
        running_ptr = running_ptr.next
    return True



init_list = [(1, "k"), (2, "a"),(2.5, "y"),(2.6, "y"),(2.7, "z"), (3, "a"), (4, "k")]
list1 = LinkedList.from_list(init_list)
print(is_linkedlist_palindrome(list1))

# XXXX Recursice!!!!
def is_palindrom2(input_list):
    size = 0
    ptr = input_list._head
    while ptr is not None:
        size += 1
        ptr = ptr.next
    result_node, result_is_palindrom = is_palindrome_recursive(input_list._head, size)
    return result_is_palindrom


def is_palindrome_recursive(node, size):
    if node is None:
        return None, True
    elif size == 1:
        return node.next, True
    elif size == 0:
        return node, True

    else:
        result_node, result_previous_palindrome = is_palindrome_recursive(node.next, size-2)
        if result_previous_palindrome is False:
            return None, False
        else:
            if node.data.value == result_node.data.value:
                return result_node.next, True
            else:
                return None, False

init_list = [(1, "k"), (2, "a"),(2.5, "y"), (3, "a"), (4, "k")]
init_list = []
list1 = LinkedList.from_list(init_list)
print(is_palindrom2(list1))