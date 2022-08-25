"""
Task 1

A simple function.

Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.
"""


def favourite_movie(name):
    print(f"My favorite movie is named {name}")


"""
Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
Make the function print out the values of the dictionary to make sure that it works as intended.
"""


def make_country(country_name, capital):
    result = {country_name: capital}
    print(result)
    return result


"""
Task 3

A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a 
first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary 
number of arguments (only numbers) as the second parameter. 
Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""


def make_operation(operator, *args: int):
    print(*args)
    for i in args:
        if type(i) != int:
            raise ValueError(f"Operands should contain only integers: {i}")
    result = 0
    if operator == "+":
        for i in args:
            result += i
    elif operator == "-":
        for i in args:
            result -= i
    elif operator == "*":
        result = 1
        for i in args:
            result *= i
    else:
        return TypeError(f"Incorrect operation: {operator}")

    return result


"""
Task1

Write a function that takes on an input random ints (between 1 and 10) 
and returns the longest consecutive run and the length of that run of elements of the list.

Ex.  def task1(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
 def task1(1) -> 1, 1
 def task1() -> 0, None

Then create another function which takes on input result of function 
from the previous step and prints Informative message about 
the longest consecutive run, something like - “Longest run is 6 of integers - 4”

"""

"""
WORK IN PROGRESS
"""


def longest_consecutive_run(*args):
    result = (0, 0)
    amount = 1
    temp_number = args[0]
    for i in range(1, len(args)):

        if args[i] != temp_number:
            if result[1] < amount:
                result = (amount, temp_number)
            temp_number = args[i]
            amount = 1
        elif i == len(args) - 1 and args[i] == temp_number:
            amount += 1
            result = (amount, temp_number)
        elif args[i] == temp_number:
            amount += 1
    return result


def message_to_user(info):
    print(f"Longest run is {info[0]} of integers - {info[1]}")


"""
Task 2

Create a function that takes on an input random ints 
(between 1 and 10) and returns the list, without duplicates. 
Try to create two versions of this function - first with usage 
set and list constructors and second only using for-in loops.

def task2(1,2,34,2,3,2,4) -> 1, 2, 34, 3, 4
"""


def exclude_dublicates_ver_1(*args):
    return list(set(args))


def exclude_dublicates_ver_2(*args):
    result = []
    for i in args:
        if i not in result:
            result.append(i)
    return result


if __name__ == "__main__":
    #favourite_movie("In Brugge")
    #make_country("Norway", "Oslo")
    #print(make_operation("*", 6, 7))
    message_to_user(longest_consecutive_run(1, 1, 2, 2, 2))
    #print(exclude_dublicates_ver_1(1,2,34,2,3,2,4))
    #print(exclude_dublicates_ver_1(1, 2, 34, 2, 3, 2, 4))
