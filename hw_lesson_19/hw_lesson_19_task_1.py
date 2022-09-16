"""
Task 1

Create your own implementation of a built-in function enumerate,
named `with_index`, which takes two parameters: `iterable` and `start`,
default is 0. Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1


if __name__ == "__main__":
    array = ["a", "b", "c", "d", "e"]
    for i in with_index(array, 4):
        print(i)
