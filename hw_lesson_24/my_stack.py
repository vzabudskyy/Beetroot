class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop()

    def top(self):
        return self.__data[-1]

    def is_empty(self):
        return self.__data == []
