def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) in [0, 1]:
        return True
    elif looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    return False


if __name__ == "__main__":
    assert is_palindrome('mom') == True
    assert is_palindrome('sassas') == True
    assert is_palindrome('o') == True
