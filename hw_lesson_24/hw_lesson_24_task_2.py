"""
Task 2

Write a program that reads in a sequence of characters,
and determines whether it's parentheses,
braces, and curly brackets are "balanced."
"""
from my_stack import Stack


def braces_check(sequence: str) -> bool:
    stack = Stack()
    braces = {")": "(", "]": "[", "}": "{"}
    for i in sequence:
        if i in braces.values():
            stack.push(i)
        elif braces[i] == stack.top():
            stack.pop()
        elif braces[i] != stack.top() and not stack.is_empty():
            return False
    return True


if __name__ == "__main__":
    print(braces_check("([{()(]}])"))

