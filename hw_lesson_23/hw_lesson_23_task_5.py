def sum_of_digits(digit_string: str) -> int:
    if digit_string.isalpha():
        raise ValueError("input string must be digit string")
    elif len(digit_string) == 1:
        return int(digit_string)
    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


if __name__ == "__main__":
    assert sum_of_digits("26") == 8
    assert sum_of_digits("1234") == 10
    