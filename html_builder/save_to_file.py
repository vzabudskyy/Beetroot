from datetime import datetime, timedelta
from time import sleep


def save(name):
    def inner(func):
        def wrapper(self):
            result = func(self)
            with open(f"{name}", "w") as file:
                file.write(result)
            return result
        return wrapper
    return inner


class Timer:
    def __init__(self, time):
        self.anchor_time = None
        self.time = datetime.strptime(time, "%H:%M:%S")

    def __call__(self):
        delta = self.time - (datetime.now() - self.anchor_time) + timedelta(microseconds=100000)
        return delta.strftime("%H:%M:%S")

    def start(self):
        self.anchor_time = datetime.now() + timedelta(microseconds=30000)


if __name__ == "__main__":
    t = Timer("00:10:10")
    t.start()
    while t() != "00:00:00":
        print(t())
        sleep(1)
