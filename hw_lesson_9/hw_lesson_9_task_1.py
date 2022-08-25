"""
Task 1

Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?
"""


def oops():
    raise IndexError


def call_oops():
    try:
        oops()
    except IndexError as ex:  # if we raise KeyError, except doesn`t catch it
        print(f"We catch IndexError {ex}")


if __name__ == "__main__":
    call_oops()
