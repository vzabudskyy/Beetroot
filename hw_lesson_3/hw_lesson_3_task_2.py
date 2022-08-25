"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""

import sys


if len(sys.argv) == 2:
    string = sys.argv[1].replace(" ", "", len(sys.argv[1]))
else:
    string = input("Enter a phone number:\n")
    string = string.replace(" ", "", len(string))

if len(string) == 10:
    if string.isdigit() is True:
        if string[0] != "7":
            print("Everything is correct")
        else:
            print("! Enemy detected !")
    else:
        print("Phone number length incorrect")
else:
    print("Too short for a phone number")
