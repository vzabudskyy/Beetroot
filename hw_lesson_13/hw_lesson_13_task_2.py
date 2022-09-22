"""
Task 2

Write a Python program to access a function inside a function (Tips: use function, which returns another function)
"""
from inspect import signature, getclosurevars, getinnerframes


def cuboid_volume(a):
    def volume(b, c):
        return a*b*c
    return volume


if __name__ == "__main__":
    result = cuboid_volume(2)
    print(result(3, 4))
