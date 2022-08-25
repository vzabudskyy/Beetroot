"""
Task1
Додати у функцію з 3-го завдання уроку 8 (A simple calculator),
обробку операції ділення. Врахувати можливий 0 у вхідних аргументах.
"""
import operator as o


def make_op(operator, *args):
    if len(args) == 1:
        return args[0]

    operands = []
    ops = {
        '+': o.add,
        '-': o.sub,
        '*': o.mul,
        '/': o.truediv
        }

    for i in args:
        if type(i) != int:
            raise ValueError(f"Operands should contain only integers: {i}")
        operands.append(i)

    operator = ops[operator]
    result = operands[0]
    for i in operands[1:]:
        result = operator(result, i)
    return result


if __name__ == "__main__":
    try:
        print(make_op("/", 4, 0, 2))
        print(make_op("*", 4, "H", 2))
        print(make_op("%", 4, 0, 2))
        print(make_op("*", 4))
    except ValueError:
        print("All operands should be integers.")
    except KeyError:
        print("Can`t recognize an operator.")
    except ZeroDivisionError:
        print("You can`t divide by zero.")
