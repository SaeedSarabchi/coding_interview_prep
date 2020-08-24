class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node:
    def __init__(self, key_value):
        self.data = key_value
        self.next = None
        self.prev = None


    ''''@property
    def data(self):
        return self.data.key, self.data.value

    @data.setter
    def data(self,key_value):
        self.data.key = key_value[0]
        self.data.value = key_value[1]'''



class LinkedList:

    def __init__(self):
        self._head = None

    @classmethod
    def from_list(cls, input_list):
        linkedlist = cls()
        for (key,value) in input_list:
            new_node = Node(KeyValue(key,value))
            linkedlist.add_node(new_node)
        return linkedlist

    def add_node(self, new_node):
        new_node.next = None
        if self._head is not None:
            self._head.prev = new_node
            new_node.next = self._head
        new_node.prev = None
        self._head = new_node

    def find_node_by_key(self, key):
        reference = self._head
        while reference is not None:
            if reference.data.key == key:
                return reference
            reference = reference.next
        raise KeyError("key not found!")

    def delete_node_by_key(self, key):
        temp = self.find_node_by_key(key)
        if temp.prev is not None:
            temp.prev.next = temp.next
        else: # if temp.prev is None it means that temp is the first element
            self._head = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev
        return temp

    def to_list_forward(self):
        reference = self._head
        list_forward = []
        while reference is not None:
            key = reference.data.key
            value = reference.data.value
            list_forward.append((key,value))
            reference = reference.next
        return list_forward

    def to_list_backward(self):
        list_backward = []
        reference = self.get_last_node()
        while reference is not None:
            key = reference.data.key
            value = reference.data.value
            list_backward.append((key,value))
            reference = reference.prev
        return list_backward

    def get_first_node(self):
        return self._head

    def get_last_node(self):
        reference = self._head
        last_node = None
        while reference is not None:
            last_node = reference
            reference = reference.next
        return last_node

    def __len__(self):
        reference = self._head
        count = 0
        while reference is not None:
            count += 1
            reference = reference.next
        return count

    def sanity_check(self):
        forward_list = self.to_list_forward()
        backward_list = self.to_list_backward()
        return True if forward_list == list(reversed(backward_list)) else False
