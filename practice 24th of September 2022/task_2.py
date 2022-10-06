

class Dumb:
    def __init__(self, file):
        self.__file = file
        self.__data = []

    def __enter__(self):
        self.__file = open(self.__file, "w")
        return self

    def send(self, data):
        self.__data.append(f"{data}\n")
        if len(self.__data) % 3 == 0:
            self.__dumb()
            self.__clear()

    def __dumb(self):
        for data in self.__data:
            self.__file.write(data)

    def __clear(self):
        self.__data = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__dumb()
        self.__file.close()


with Dumb("dumb.txt") as dumb:
    for _ in range(5):
        dumb.send("Text")
