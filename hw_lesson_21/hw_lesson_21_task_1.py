"""
Task 1

File Context Manager class

Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method,
which has to cover all the requirements to context managers mentioned here:
"""


class MyOpen:
    counter = 0

    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs
        self.__file = open(*self.__args, **self.__kwargs)
        print(f"File was opened successfully.")

    def __enter__(self):
        MyOpen.counter += 1
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        if exc_type is not None:
            print(f"The {exc_type.__name__} exception was occured.")
        print(f"MyOpen my-build-in-function was used {MyOpen.usage()} times.")

    def close(self):
        self.__file.close()
        print("File was closed successfully.")

    @classmethod
    def usage(cls):
        return cls.counter


if __name__ == "__main__":
    with MyOpen("test.txt", "r", encoding="utf8") as file:
        s = file.read()
    ss = open("test.txt", "a", encoding="latin1")
    ss.write(" TEST")
