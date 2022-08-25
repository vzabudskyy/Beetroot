from os.path import abspath
import sys


def count_lines(name):
    with open(name, "r") as file:
        amount = len(file.readlines())
    return amount


def count_chars(name):
    with open(name, "r") as file:
        amount = len(file.read().replace("\n", ""))
    return amount


def test(name):
    path = abspath(name)
    chars_amount = count_chars(path)
    lines_amount = count_lines(path)
    return chars_amount, lines_amount


if __name__ == "__main__":
    file_name = sys.argv[1]
    chars, lines = test(file_name)
    print(f"{file_name} {lines} {chars}")
