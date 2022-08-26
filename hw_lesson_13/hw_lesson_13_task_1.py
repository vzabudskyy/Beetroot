"""
Task 1

Write a Python program to detect the number of local variables declared in a function.
"""
import test_functions_task_1
from inspect import getmembers, isfunction, getsource


def count_locals(func):
    return func.__code__.co_nlocals


def show(array):
    for i in array:
        print(f"Function name: '{i[0]}'\nLocal declared variables: {i[1]}\nSource:\n{i[2]}")


def main():
    names_of_func, all_funcs = zip(*getmembers(test_functions_task_1, isfunction))
    result = zip(names_of_func, map(count_locals, all_funcs), map(getsource, all_funcs))
    show(result)


if __name__ == "__main__":
    main()
