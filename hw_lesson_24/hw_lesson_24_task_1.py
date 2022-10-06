"""
Task 1

Write a program that reads in a sequence of characters and
prints them in reverse order, using your implementation of Stack.
"""

from my_stack import Stack


def reverse_order_using_stack(word: str) -> str:
    stack = Stack()
    length = len(word)
    for i in range(0, 2 * length + 1):
        if i < length:
            stack.push(word[i])
        elif i == length:
            word = ""
        else:
            word += stack.pop()
    return word


if __name__ == "__main__":
    print(reverse_order_using_stack("hello"))
