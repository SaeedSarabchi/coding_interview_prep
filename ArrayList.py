class ArrayList:
    def __init__(self, init_size):
        self.__orig_list = [None]*init_size
        self.__orig_len = init_size
        self.__len = 0

    @property
    def orig_list(self):
        return self.__orig_list

    @property
    def orig_len(self):
        return self.__orig_len

    def __len__(self):
        return self.__len

    def append(self, value):
        if self.__len == self.__orig_len:
            self.__double_the_size()
        self.__orig_list[self.__len] = value
        self.__len += 1

    def __double_the_size(self):
            new_array = [None] * self.__orig_len * 2
            new_array[:self.__orig_len] = self.__orig_list
            self.__orig_list = new_array
            self.__orig_len = self.__orig_len * 2
