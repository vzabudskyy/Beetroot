"""
Task 1

Primes

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

We have the following input list of numbers, some of them are prime.
You need to create a utility function that takes as input a number
and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different
concurrent implementations for filtering NUMBERS.

Compare the results and performance of each of them.
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math
from functools import wraps
from datetime import datetime


NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def check_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        delta = end - start
        print(f"{func.__name__} was executed in {delta}")
        return result
    return wrapper


def isprime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

        # To check through all numbers of the form 6k ± 1
    # until i <= square root of n, with step value 6
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False

    return True


@check_execution_time
def one_by_one():
    return [isprime(num) for num in NUMBERS]


@check_execution_time
def processing_version():
    with ProcessPoolExecutor(max_workers=5) as executor:
        result = [num for num in executor.map(isprime, NUMBERS)]
        return result


if __name__ == "__main__":
    print(processing_version())
