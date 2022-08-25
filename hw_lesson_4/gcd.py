"""
Greatest common denominator
"""


def gcd(first_num, second_num):
    if first_num == 0 and second_num == 0:
        return "Error"
    elif first_num == 0:
        divisor = second_num
    elif second_num == 0:
        divisor = first_num
    elif first_num > second_num:
        divisor = second_num
    else:
        divisor = first_num

    while True:
        reminder_first = first_num % divisor
        reminder_second = second_num % divisor
        if reminder_first == 0 and reminder_second == 0:
            return divisor
        else:
            divisor -= 1


def print_table(table):
    for i in table:
        print(f"{i}\n")
