"""
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10,
and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
"""
import random


random_nums_1 = []
random_nums_2 = []
while len(random_nums_1) != 10:
    random_nums_1.append(random.randint(0, 10))
    random_nums_2.append(random.randint(0, 10))
"""
random_nums_1 = [random.randint(0, 10) for i in range(10)]
random_nums_2 = [random.randint(0, 10) for i in range(10)]

I think, this is more convenient way.
"""
print(f"First list: {random_nums_1}\nSecond list: {random_nums_2}")

unique_list = list(set(random_nums_1).intersection(set(random_nums_2)))
print(f"Unique numbers: {unique_list}")
