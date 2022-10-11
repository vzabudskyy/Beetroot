"""
Task 3

Implement a queue using a singly linked list.
"""
from hw_lesson_26_task_1 import OrderedList


class Queue:
    def __init__(self):
        self._items = OrderedList()

    def is_empty(self):
        return self._items.is_empty()

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return self._items.size()

    def __repr__(self):
        representation = "<Queue>\n"
        length = self._items.size()
        for item in range(length, 0, -1):
            representation += f"{length - item + 1}: {self._items[item - 1]}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue('cat')
    q.enqueue('frog')
    q.enqueue(True)
    print(q)
    print(f"Size: {q.size()}")
    q.dequeue()
    print(q)
    [q.dequeue() for i in range(4)]
    print(f"Is empty: {q.is_empty()}")
    print(q)
