"""
Task 3

The math quiz program.

Write a program that asks the answer for a mathematical expression,
checks whether the user is right or wrong, and then responds with a message accordingly.
"""

answer = input("Type only digit: \n\t2x^2 + 4x = -2 \n\n Answer: ")
if int(answer) == -1:
    print("Right answer")
else:
    print("Wrong answer")

