from LinkedList import LinkedList, Node, KeyValue


class HashTable:
    _INIT_SIZE = 2

    def __init__(self):
        self.__array_list = [None]* HashTable._INIT_SIZE
        self.__num_of_elements = 0

    def hash_to_list(self):
        hash_to_list = []
        for linked_list_head in self.__array_list:
            if linked_list_head is not None:
                hash_to_list.append(linked_list_head.to_list_forward())
            else:
                hash_to_list.append(None)
        return hash_to_list

    def __hash_map(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % len(self.__array_list)

    def __getitem__(self, key):
        found_node = self.__find_node_by_key(key)
        return found_node.data.value

    def __find_node_by_key(self, key):
        linked_list_head = self.__array_list[self.__hash_map(key)]
        if linked_list_head is None:
            raise KeyError
        found_node = linked_list_head.find_node_by_key(key)
        return found_node

    def __setitem__(self, key, value):
        found_node = None
        try:
            found_node = self.__find_node_by_key(key)
        except KeyError: # key not found
            self.__put_key_value(key, value)
            if self.__num_of_elements > len(self.__array_list):
                self.__double_the_size()
                self.__rehash()
        else:
            found_node.data.value = value

    def __put_key_value(self, key, value):
        hash_index = self.__hash_map(key)
        if self.__array_list[hash_index] is None:
            self.__array_list[hash_index] = LinkedList()
        new_node = Node(KeyValue(key,value))
        self.__array_list[hash_index].add_node(new_node)
        self.__num_of_elements += 1

    def __double_the_size(self):
        new_array_list = [None]*len(self.__array_list)*2
        new_array_list[:len(self.__array_list)] = self.__array_list
        self.__array_list = new_array_list

    def __delitem__(self, key):
        linked_list = self.__array_list[self.__hash_map(key)]
        linked_list.delete_node_by_key(key)
        if len(linked_list) == 0:
            self.__array_list[self.__hash_map(key)] = None

    def __clear(self):
        self.__array_list = [None]*len(self.__array_list)
        self.__num_of_elements = 0

    def __rehash(self):
        all_elements = self.hash_to_list()
        self.__clear()
        for element_list in all_elements:
            if element_list is not None:
                for (key, value) in element_list:
                    self.__put_key_value(key, value)


