"""
Task 2

Write a function that takes in two numbers from the user via input(),
call the numbers a and b, and then returns the value of squared a divided by b,
construct a try-except block which raises an exception
if the two values given by the input function were not numbers,
and if value b was zero (cannot divide by zero).
"""


def get_int_operands():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b


def test(a, b):
    try:
        return a**2/b
    except ValueError:
        print("Values should be digits.")
    except ZeroDivisionError:
        print("You can't divide by zero.")


if __name__ == "__main__":
    x, y = get_int_operands()
    print(test(x, y))
