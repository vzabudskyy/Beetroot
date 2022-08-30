"""
Task 1

Write a decorator that prints a function with arguments passed to it.

NOTE! It should print the function, not the result of its execution!

For example:

 "add called with 4, 5"

```

def logger(func):

    pass



@logger

def add(x, y):

    return x + y



@logger

def square_all(*args):

    return [arg ** 2 for arg in args]

```
"""


def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {str(args)[1:-1]}")
        return func(*args)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == "__main__":
    result1 = add(1, 2)
    result2 = square_all(1, 2, 3, 4, 5)
