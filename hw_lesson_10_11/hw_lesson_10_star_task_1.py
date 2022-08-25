"""
Створити функцію, яка перетворює рядок в число без використання стандартних функцій. Спробуйте зробити без гугління.
"""
import operator as o


digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}


def to_str(some_str):
    result = 0

    if some_str[0] == "-":
        operator = o.sub
        sign_index = -len(some_str)
    else:
        operator = o.add
        sign_index = -len(some_str) - 1

    if "." in some_str:
        float_part = -(len(some_str)-some_str.index("."))
        place = 10**(float_part+1)
        for i in some_str[-1:float_part:-1]:
            result = operator(result, digits[i] * place)
            place *= 10
    else:
        float_part = -1

    place = 1

    for i in some_str[float_part-1:sign_index:-1]:
        result = operator(result, digits[i]*place)
        place *= 10

    return round(result, -float_part)


if __name__ == "__main__":
    converted = to_str('-212321.12979832')
    print(f"{converted} : {type(converted)}")
