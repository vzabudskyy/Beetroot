"""
Task 2

Create your own implementation of a built-in function range,
named in_range(), which takes three parameters: `start`, `end`,
and optional step. Tips: See the documentation for `range` function
"""


def in_range(*args):
    length = len(args)
    if not all(isinstance(i, int) for i in args):
        raise ValueError
    elif length == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif length == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif length == 1:
        start = 0
        stop = args[0]
        step = 1
    else:
        raise TypeError("in_range expected 1 argument, got 0")

    if step/abs(step) != stop/abs(stop):
        raise ValueError
    elif step > 0:
        statement = int.__lt__
    else:
        statement = int.__gt__

    while statement(start, stop):
        yield start
        start += step


if __name__ == "__main__":
    for num in in_range(-1, -9, -1):
        print(num)
