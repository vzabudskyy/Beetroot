"""
Task 4

Custom exception

Create your custom exception named `CustomException`,
you can inherit from base Exception class,
but extend its functionality to log every error message
to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file

```

class CustomException(Exception):

def __init__(self, msg):
"""
from time import time, ctime


class CustomException(Exception):
    def __init__(self, msg):
        with open("logs.txt", "a") as file:
            file.write(f"CustomException was raised at {ctime(time())}\nMessage: {msg}\n\n")


if __name__ == "__main__":
    try:
        CustomException("First exception")
        ex = CustomException("Second exception")
        raise CustomException("Third exception")

    except CustomException:
        with open("logs.txt", "r") as file:
            logs = file.read()
            print(logs)
