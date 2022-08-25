"""
Task1

Write a Python program to construct the following pattern, using a while loop

*

* *

* * *

* * * *

* * * * *

* * * *

* * *

* *

*

Плюс за можливість динамічно змінити максимальну кількість зірочок в одному рядку (в прикладі 5)
"""

import sys


if len(sys.argv) == 2:
    amount_per_line = int(sys.argv[1])
else:
    amount_per_line = int(input("Enter max quantity of stars in one line:\n"))
i = 0

while 2*amount_per_line > i:
    i += 1
    if i < amount_per_line:
        print(i*"*")
    else:
        print((2*amount_per_line-i)*"*")
