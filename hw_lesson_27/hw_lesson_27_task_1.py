"""
Task 1

Implement binary search using recursion
"""
from math import ceil


def binary_search(sequence, element, low=0, high=None):
    if high is None:
        high = len(sequence) - 1
    mid = ceil((low + high) / 2)
    guess = sequence[mid]
    if guess == element:
        return mid
    elif guess < element:
        return binary_search(sequence, element, mid, high)
    return binary_search(sequence, element, low, mid)


if __name__ == "__main__":
    s = [i for i in range(101)]
    print(s)
    print(binary_search(s, 27))
