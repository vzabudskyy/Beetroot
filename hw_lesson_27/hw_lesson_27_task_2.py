"""
Task 2

Read about the Fibonacci search and implement it using python.
Explore its complexity and compare it to sequential, binary searches.
"""


def fibonacci_search(lst, x):
    fibm2 = 0
    fibm1 = 1
    fibm = fibm1 + fibm2
    while fibm < len(lst):
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm1 + fibm2
    index = -1
    while fibm > 1:
        guess = min(index + fibm2, len(lst)-1)
        if lst[guess] < x:
            fibm = fibm1
            fibm1 = fibm2
            fibm2 = fibm - fibm1
            index = guess
        elif lst[guess] > x:
            fibm = fibm2
            fibm1 = fibm1 - fibm2
            fibm2 = fibm - fibm1
        else:
            return guess


if __name__ == "__main__":
    for i in range(1, 12):
        print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], i))

