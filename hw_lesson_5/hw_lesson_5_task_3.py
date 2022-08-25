"""
Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100,  then find all integers
from the list that are divisible by 7 but not a multiple of 5,
and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration
"""

"""
More convenient way:
    sample = [i for i in range(1, 101)]
"""
sample = []
while len(sample) != 100:
    sample.append(len(sample)+1)
result = []
print(f"Sample: {sample}")
k = 0
while k < len(sample):
    if sample[k] % 7 == 0 and sample[k] % 5 != 0:
        result.append(sample[k])

    k += 1

print(f"Result: {result}")
