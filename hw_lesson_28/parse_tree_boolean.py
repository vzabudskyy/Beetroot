"""
Task 2

Modify the `build_parse_tree` and `evaluate functions to
handle boolean statements (and, or, and not). Remember
that “not” is a unary operator, so this will somewhat
complicate your code.

"""


import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def splitter(math_expr: str) -> List[str]:  # Task 1
    result = []
    statement = ""
    for char in math_expr:
        if char == " ":
            result.append(statement)
            statement = ""
        elif char in ['(', ')']:
            if statement:
                result.append(statement)
                statement = ""
            result.append(char)
        elif char.isalpha():
            statement += char

    return result


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = splitter(math_exp)
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree
    convert_bool = {"True": True, "False": False}

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['and', 'or', "not"]:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')' or current_tree.get_root_val() == "not":
            current_tree = stack.pop()

        elif i in convert_bool:
            try:
                current_tree.set_root_val(convert_bool[i])
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates = {'and': operator.and_, 'or': operator.or_, 'not': operator.not_}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    elif right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        if isinstance(tree.get_root_val(), int):
            s_val = s_val + str(tree.get_root_val())
        else:
            s_val = '(' + print_exp(tree.get_left_child()) + " "
            s_val = s_val + str(tree.get_root_val())
            s_val = s_val + " " + print_exp(tree.get_right_child()) + ')'

    return s_val


if __name__ == "__main__":
    test1 = "not (True and (False or not True))"
    test2 = "(True and (True or False))"
    pt: BinaryTree = build_parse_tree(test1)
    print(evaluate(pt))
    print()
    pt.pre_order()
    print()
    pt.post_order()
    print()
    pt.in_order()
    print("__")
    print(print_exp(pt))

