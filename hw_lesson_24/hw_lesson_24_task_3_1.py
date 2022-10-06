"""
Task 3

Extend the Stack to include a method called get_from_stack
that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order.
Consider the case in which the element is not found -
raise ValueError with proper info Message



Extend the Queue to include a method called get_from_stack
that searches and returns an element e from a queue.
Any other element must remain in the queue respecting their order.
Consider the case in which the element is not found -
raise ValueError with proper info Message
"""


class Stack:
    def __init__(self):
        self.__data = []

    def get_from_stack(self, item):
        saved = []
        while True:
            current = self.pop()
            if current == item:
                break
            saved.append(current)

        for i in saved[-1::-1]:
            self.push(i)

    def size(self):
        return len(self.__data)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self.__data), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop()

    def top(self):
        return self.__data[-1]

    def is_empty(self):
        return self.__data == []


if __name__ == "__main__":
    s = Stack()
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [s.push(i) for i in seq]
    print(s)
    s.get_from_stack(5)
    print(s)