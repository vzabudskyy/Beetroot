"""
Task 2

Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers.
You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list
directly via access to attribute, use getters and setters instead!
"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, worker):
        if isinstance(worker, Worker):
            self.__workers.append(worker)
        else:
            raise ValueError

    def add_worker(self, worker):
        self.workers.append(worker)
        worker.boss = self

    def __str__(self):
        return f"{self.name}"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self.__boss = boss
            boss.workers.append(self)

    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
    b = Boss(1, "Big Boss", "DATBS")
    w = Worker(1, "John Doe", "DATBS", b)
    print(w.boss)
    print(b.workers[0])
