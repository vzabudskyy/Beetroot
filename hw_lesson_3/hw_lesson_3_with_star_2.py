"""
Task2

Write a python program, which sums all digits in a python string.

Examples, input - ‘1234’, output - 10
"""

import sys


if len(sys.argv) == 2:
    string = sys.argv[1]
else:
    string = input("Enter string of digits:\n")

if string.isdigit() is True:
    print(f"Result first way: {eval('+'.join(list(string)))}")
    result = 0
    for i in string:
        result += int(i)
    print(f"Result second way: {result}")
else:
    print("Incorrect input")

