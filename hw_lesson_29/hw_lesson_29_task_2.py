"""
Task 2

Using the BinaryHeap class, implement a new class called PriorityQueue.
Your PriorityQueue class should implement the constructor, plus the enqueue and dequeue methods.
"""
from hw_lesson_29_task_1 import BinHeap


class PriorityQueue:
    def __init__(self):
        self.data = BinHeap()

    def enqueue(self, item):
        self.data.insert(item)

    def dequeue(self):
        self.data.del_max()

    def peek(self):
        return self.data.max()


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(10)
    pq.enqueue(16)
    pq.enqueue(13)
    print(pq.peek())
    pq.dequeue()
    print(pq.peek())
    pq.dequeue()
    print(pq.peek())
    pq.dequeue()
