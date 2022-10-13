"""
Task 1

Implement a binary heap as a max heap.
"""

# p - position
# 2p - left child 2p + 1 right child
from typing import List
from random import shuffle


class BinHeap:

    def __init__(self) -> None:
        self.heap_list: List[int] = [0]
        self.current_size: int = 0

    def perc_up(self, i) -> None:
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def perc_down(self, i) -> None:
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def max_child(self, i) -> int:
        if i * 2 + 1 > self.current_size:
            return i * 2
        if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def del_max(self) -> int:
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, items: List[int]) -> None:
        i = len(items) // 2
        self.current_size = len(items)
        self.heap_list = [0] + items[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def insert(self, item) -> None:
        self.heap_list.append(item)
        self.current_size += 1
        self.perc_up(self.current_size)

    def max(self):
        return self.heap_list[1]


if __name__ == "__main__":
    tree_list = [9, 5, 6, 8, 1, 3]
    tree_list2 = [1, 3, 6, 5, 9, 8]
    bh = BinHeap()
    for _ in range(10):
        shuffle(tree_list)
        bh.build_heap(tree_list)
        print(f"Test list: {tree_list}\nBuilded tree: {bh.heap_list}\n")
        print(bh.del_max())
        print(bh.heap_list)