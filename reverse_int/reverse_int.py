"""
123456, n = 3 -> 456123| 123456, 10 -> 
"""


def reverse_int(number, n):
    number_len = 0
    divisor = 1
    result = number

    while (number // divisor) != 0:
        divisor *= 10
        number_len += 1

    n = n % number_len

    for i in range(n):
        last = result % 10
        result = result // 10 + last*10**(number_len - 1)

    return result


if __name__ == "__main__":
    print(reverse_int(123000, 4))

