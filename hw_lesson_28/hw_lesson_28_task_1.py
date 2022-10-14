"""
Task 1

Extend the `build_parse_tree` function to handle mathematical expressions
that do not have spaces between every character.
"""
from typing import List


class Tree:
    def __init__(self, data = ''):
        self.data: str = data
        self.left_node: 'Tree' = None
        self.right_node: 'Tree' = None

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{self.data}"

    def traverse(self):
        if self.left_node:
            self.left_node.traverse()
        if self.right_node:
            self.right_node.traverse()
        print(self.data)


def build_node(root, expr):
    if expr and expr[0] == "(":
        root.left_node = Tree()
        expr = build_node(root.left_node, expr[1:])

    if expr and expr[0].isdigit():
        root.left_node = Tree()
        root.left_node.data = int(expr[0])
        expr = expr[1:]

    if expr and expr[0] in ["+", "//", "-", "*"]:
        root.data = expr[0]
        expr = expr[1:]

    if expr and expr[0].isdigit():
        root.right_node = Tree()
        root.right_node.data = int(expr[0])
        expr = expr[1:]
    elif expr:
        root.right_node = Tree()
        expr = build_node(root.right_node, expr[1:])

    if not expr:
        return

    if expr[0] == ")":
        return expr[1:]


def build_tree(expr: str) -> Tree:
    tree = Tree()
    expr: List[str] = [i for i in expr if i != " "]
    build_node(tree, expr)
    return tree


def calculate_expresion(expresion: str):
    tree = build_tree(expresion)
    return tree.traverse()


if __name__ == "__main__":
    math_expresion = '( ( 1 + 5 ) * 3 )'
    print(calculate_expresion(math_expresion))
