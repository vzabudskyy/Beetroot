"""
Task 2

Implement a stack using a singly linked list.
"""
from hw_lesson_26_task_1 import OrderedList


class Stack:
    def __init__(self):
        self.__data = OrderedList()

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop()

    def top(self):
        return self.__data[self.__data.size()-1]

    def is_empty(self):
        return self.__data.is_empty()

    def __repr__(self):
        representation = "<Stack>\n"
        length = self.__data.size()
        for item in range(length, 0, -1):
            representation += f"{length - item + 1}: {self.__data[item - 1]}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()
    seq = [1, 2, 3]
    [s.push(i) for i in seq]
    print(f"Check is empty: {s.is_empty()}")
    print(s)
    print(f"Top: {s.top()}")
    print(f"Pop: {s.pop()}")
    print(f"Top: {s.top()}")
    print(s)
    print(f"Pop: {s.pop()}")
    print(f"Pop: {s.pop()}")
    print(f"Check is empty: {s.is_empty()}")