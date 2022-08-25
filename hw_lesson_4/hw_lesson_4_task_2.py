"""
Task 2

The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”
"""

name, age = input("Enter your name: \n"), input("Enter your name age: \n")
print(f"Hello {name}, on your next birthday you’ll be {int(age)+1} years")
