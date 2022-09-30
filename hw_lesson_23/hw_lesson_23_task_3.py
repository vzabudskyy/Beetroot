def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError("This function works only with postive integers")
    elif n == 1:
        return a
    return a + mult(a, n - 1)


if __name__ == "__main__":
    assert mult(2, 4) == 8
    assert mult(2, 0) == 0
