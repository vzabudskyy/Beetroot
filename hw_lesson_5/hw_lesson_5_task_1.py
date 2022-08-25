"""
Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
"""
import random


random_nums = []
while len(random_nums) != 10:
    random_nums.append((random.randint(0, 100)))
print(f"Input list: {random_nums}")
k = 0
minimum = random_nums[k]
while k < len(random_nums) - 1:
    if minimum > random_nums[k+1]:
        minimum = random_nums[k+1]
    k += 1
print(f"Min: {minimum}")
