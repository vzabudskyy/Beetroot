"""

"""


from gcd import gcd, print_table

"""
To be honest, I`m not sure, that this way of using generator is adequate enough and readable to use in real cases.
Anyway, I found it very interesting, because I didn't use if/else in generators before.
"""


def main():
    n = int(input("Enter the number: \n"))
    matrix = [["*" if gcd(k, i) == 1 else "_" for i in range(n)] for k in range(n)]
    print_table(matrix)


if __name__ == "__main__":
    main()
