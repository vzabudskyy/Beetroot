"""
Task 1

Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares
and cubic for an input number. Schedule the execution of this code using asyncio.gather
for a list of integers from 1 to 10. You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
ime the execution of both realizations, explore the results, what realization is more effective,
why did you get a result like this.
"""
from hw_lesson_34.hw_lesson_34_task_3 import check_execution_time
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    n1 = 0
    n2 = 1
    if n <= 0:
        raise ValueError("n should be greater then 0")
    elif n in [1, 2]:
        return n - 1
    for _ in range(2, n):
        next_n2 = n1 + n2
        n1 = n2
        n2 = next_n2
    return n2


def fac(n):
    result = n
    for _ in range(n-1, 1, -1):
        n -= 1
        result *= n
    return result


def sqr(n):
    return n**2


def cbc(n):
    return n ** 3


def fill_list(func, input_list, output_list):
    for elem in input_list:
        result = func(elem)
        output_list.append(result)


@check_execution_time
def main(input_list, output_dict):
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.submit(fill_list, fib, input_list, output_dict["Fibonacci"],
                        fill_list, fac, input_list, output_dict["Factorial"],
                        fill_list, sqr, input_list, output_dict["Squares"],
                        fill_list, cbc, input_list, output_dict["Cubics"])


if __name__ == "__main__":
    out = {"Fibonacci": [],
           "Factorial": [],
           "Squares": [],
           "Cubics": []}

    nums = [i for i in range(1, 201)]

    main(nums, out)

    