class StringBuilder:
    _INIT_SIZE = 2

    def __init__(self):
        self.__orig_list = [None] * StringBuilder._INIT_SIZE
        self.__number_of_elements = 0

    @property
    def orig_list(self):
        return self.__orig_list

    @property
    def orig_len(self):
        return len(self.__orig_list)

    def __len__(self):
        return self.__number_of_elements

    def append(self, value):
        try:
            to_be_appended = str(value)
            for char in to_be_appended:
                if self.__number_of_elements == len(self.__orig_list):
                    self.__double_the_size()
                self.__orig_list[self.__number_of_elements] = char
                self.__number_of_elements += 1
        except:
            raise ValueError("input value cannot be converted into string")

    def __double_the_size(self):
            new_array = [None] * len(self.__orig_list) * 2
            new_array[:len(self.__orig_list)] = self.__orig_list
            self.__orig_list = new_array

