"""
Task 3

Create your own implementation of an iterable,
which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
"""


class MyIterable:
    def __init__(self, *args):
        self.content = list(args)
        self.max = len(args)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n == self.max:
            raise StopIteration

        result = self.content[self.n]
        self.n += 1
        return result

    def __getitem__(self, index):
        return self.content[index]


if __name__ == "__main__":
    for i in MyIterable(1, 2, 3, 4, 5, 6):
        print(i)

    ll = MyIterable(1, 2, 3, 4, 5, 6)
    print(ll[3])