"""
Task3

Write a Python program that accepts a string and calculate the number of digits,
letters and other characters in the input string
"""
import sys


if len(sys.argv) == 2:
    string = sys.argv[1]
else:
    string = input("Enter string:\n")

counter = [0, 0, 0]
for i in string:
    if i.isalpha():
        counter[0] += 1
    elif i.isdigit():
        counter[1] += 1
    else:
        counter[2] += 1
print(f"Result: \nLetters: {counter[0]}\nDigits: {counter[1]}\nCharacters: {counter[2]}")
