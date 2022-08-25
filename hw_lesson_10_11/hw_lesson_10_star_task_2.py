"""
Створити функцію, яка приймає на вхід список та число n.
Вхідний список потрібно розбити на n максимально рівномірних підсписків.
Додатково можна зробити аргумент, який дозволить перевернути кожен із підсписків.
"""
from math import ceil,trunc


def split(array, n):

    if len(array) <= n:
        return array

    array_1 = array[0:len(array)//2]
    array_2 = array[len(array)//2:len(array)]
    result = [split(array_1, n)] + [split(array_2, n)]
    return result


def split_2(array, n, reverse=False):
    result = []
    length = len(array)
    step = length / n

    if ceil(step)*n - length >= step:
        step = trunc(step)
    else:
        step = ceil(step)

    for i in range(0, length, step):
        if len(result) + 1 == n:
            result.append(array[i:length])
            break
        else:
            result.append(array[i:i + step])
    return result


if __name__ == "__main__":
    mas2 = split_2([1,2,3,4,5,6,7,8,9,10,11, 12], 9)
    print(mas2)
