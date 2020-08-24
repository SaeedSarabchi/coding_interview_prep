from LinkedList import *

#XXXX Python parameter assignment is by reference, but the reference is by Value!!!!!!!
def delete_middle_node(node):
    node.data.value = "salaaaaaaame garm"
    print(id(node))
    node.data = node.next.data
    node.next = node.next.next
    print(id(node))

    #print(node.data.key)


init_list = [(4, "val4"), (3, "val3"), (2, "val2"), (1, "val1")]
lili = LinkedList.from_list(init_list)
ptr = lili._head
print(id(ptr))
print(id(ptr.next))
print(id(ptr.next.next))
delete_middle_node(ptr.next)
print(lili.to_list_forward())




