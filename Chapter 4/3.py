from LinkedList import LinkedList, Node
from BSTree import BSTree, BSTreeNode


def create_linkedlist_per_tree_level(tree):
    first_linked_list = LinkedList()
    first_linked_list.add_node(Node(tree._root))
    linked_lists = []
    if tree._root is None:
        return linked_lists
    linked_lists = [first_linked_list]
    list_cntr = 1
    while True:
        new_level = LinkedList()
        previous_level_ref = linked_lists[list_cntr-1]._head
        while previous_level_ref is not None:
            if previous_level_ref.data.left is not None:
                new_level.add_node(Node(previous_level_ref.data.left))
            if previous_level_ref.data.right is not None:
                new_level.add_node(Node(previous_level_ref.data.right))
            previous_level_ref = previous_level_ref.next
        if (new_level._head == None):
            break
        linked_lists.append(new_level)
        list_cntr += 1
    return linked_lists

tree = BSTree()
tree.insert_key(6)
tree.insert_key(7)
tree.insert_key(1)
tree.insert_key(5)
tree.insert_key(3)
tree.insert_key(2)
tree.insert_key(3.4)
result = create_linkedlist_per_tree_level(tree)
print(result)

