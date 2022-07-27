
class Iterable:
    """
    Class used to implement the iterable data structure
    """
    def __init__(self, new_list=None):
        if new_list == None:
            new_list = []
        self.__data = new_list

    @staticmethod
    def sort(data, comparison_function):
        """
        We sort the data using comb sort. (A variant of bubble sort, but instead of having the gap between numbers always
        equal to 1, the idea of comb sort is that the gap can be greater than that at the beginning but then it grows
        smaller after every iteration)
        :param data: The data we want to sort
        :param comparison_function: the function used to compare the values
        :return: the sorted data
        """
        data_copy = data[:]

        gap = len(data_copy)
        swap = True
        while gap > 1 or swap:
            gap = max(1, int(gap/1.25))
            swap = False

            for i in range(len(data_copy) - gap):
                j = i + gap
                if comparison_function(data_copy[i], data_copy[j]):
                    data_copy[i], data_copy[j] = data_copy[j], data_copy[i]
                    swap = True

        return data_copy


    @staticmethod
    def filter(data, filter_function):
        """
        Function to filter the data
        :param data: The data we want to filter
        :param filter_function: The function we use to decide whether a value passes the filter or not
        :return: the filtered data
        """
        filtered = []
        for value in data:
            if filter_function(value):
                filtered.append(value)

        return filtered

    def append(self, value):
        """
        Appends a value at the end of the list
        :param value: The value we want to append
        :return: -
        """
        self.__setitem__(len(self.__data), value)

    def remove(self, item):
        """
        Removes the item
        :param item:
        :return:
        """
        self.__data.remove(item)

    def __setitem__(self, key, value):
        """
        Sets the item at -key- to -value-
        :param key: the index
        :param value: the value
        :return: -
        """
        if key < len(self.__data):
            self.__data[key] = value
        elif key == len(self.__data):
            self.__data.append(value)
        else:
            raise IndexError

    def __getitem__(self, item):
        """
        :param item: the index
        :return: the item at the given index
        """
        return self.__data[item]

    def __delitem__(self, key):
        """
        Delete an item at the given index
        :param key: the index
        :return: -
        """
        self.__data.remove(key)

    def __next__(self):
        """
        :return: the next element during an iteration
        """
        if self.__iterator < len(self.__data) - 1:
            self.__iterator += 1
            return self.__data[self.__iterator]
        else:
            raise StopIteration

    def __iter__(self):
        """
        Function to initialize the iterator
        :return: the object to be iterated
        """
        self.__iterator = -1
        return self

    def __len__(self):
        """
        :return: The length of the data
        """
        return len(self.__data)

    def __eq__(self, other):
        """
        :param other: other data
        :return: whether the 2 sets of data are equal or not
        """
        return self.__data == other

