"""
Task 1

The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""


import random

generated_number = random.choice(range(1, 11))
user_number = int(input("Enter your number from 1 to 10:\n"))
message = None
if user_number == generated_number:
    message = "Congratulations"
else:
    message = "Oops! Wrong number"


print(f"{message}\n\tComputer number: {generated_number}\n\tYour number: {user_number}")
