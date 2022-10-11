"""
Task 1

Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and
going up to but not including the stop position.
"""
from node import Node


class OrderedList:

    def __init__(self):
        self._head = None

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

    def insert(self, index, data):
        if index == 0:
            new_head = Node(data)
            new_head.set_next(self._head)
            self._head = new_head
            return
        elif index == self.size() - 1:
            self.append(data)
            return

        node = self._head
        for _ in range(index - 1):
            node = node.get_next()

        new_node = Node(data)
        new_node.set_next(node.get_next())
        node.set_next(new_node)

    def append(self, new_node):
        if self._head is None:
            self._head = Node(new_node)
            self._head.set_next(None)
            return

        node = self._head
        while node.get_next() is not None:
            node = node.get_next()
        if isinstance(new_node, Node):
            node.set_next(new_node)
            return
        node.set_next(Node(new_node))

    def pop(self, index=None):
        if not index:
            index = self.size() - 1

        if self.size() == 1:
            result = self._head
            self._head = None
            return result

        node = self._head
        for _ in range(index - 1):
            node = node.get_next()

        result = node.get_next()
        node.set_next(result.get_next())
        return result

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self._head)
            self._head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def is_empty(self):
        return self._head is None

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __getitem__(self, index):
        if isinstance(index, slice):
            indexes = [i for i in [index.start, index.stop, index.step] if i is not None]
            if len(indexes) > 2:
                raise ValueError
            statement = range(indexes[0], indexes[1])
            result = OrderedList()
        else:
            statement = range(index)
            result = None

        node = self._head

        for _ in statement:
            if result is not None:
                result.append(node.get_data())
            node = node.get_next()

        if result is not None:
            return result
        return node.get_data()

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = OrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))
    print(my_list)
    my_list.append(150)
    print(my_list)
    my_list.pop()
    print(my_list)
    my_list.insert(3, 33)
    print(my_list)
    print(my_list[2])
    my_list.insert(0, 1000)
    print(my_list)
