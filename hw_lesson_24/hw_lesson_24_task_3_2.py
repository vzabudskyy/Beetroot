
class Queue:
    def __init__(self):
        self._items = []

    def get_from_queue(self, item):
        for _ in range(self.size()):
            current = self.dequeue()
            if current == item:
                continue
            self.enqueue(current)

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
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
    q.get_from_queue('cat')
    print(q)