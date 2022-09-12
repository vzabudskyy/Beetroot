"""
Task 3

Fraction

Створіть клас Fraction, який буде представляти всю базову арифметичну
логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок.
Потрібно додати магічні методи для математичних операцій та
операції порівняння між об'єктами класу Fraction
"""
from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) != int or type(denominator) != int:
            raise ValueError
        elif denominator == 0:
            raise ZeroDivisionError
        else:
            self.numer = numerator
            self.denom = denominator

    def reduce_fraction(self):
        divisor = gcd(self.numer, self.denom)
        self.numer //= divisor
        self.denom //= divisor
        return self

    def lcm(self, other):
        if self.denom > other.denom:
            greater = self.denom
        else:
            greater = other.denom

        while True:
            if (greater % self.denom == 0) and (greater % other.denom == 0):
                lcm = greater
                break
            greater += 1

        return lcm

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_denom = self.lcm(other)
            new_numer = self.numer * (new_denom/self.denom) + other.numer * (new_denom/other.denom)
            if new_numer == 0:
                return 0
            else:
                return Fraction(int(new_numer), new_denom).reduce_fraction()
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_denom = self.lcm(other)
            new_numer = self.numer * (new_denom/self.denom) - other.numer * (new_denom/other.denom)
            if new_numer == 0:
                return 0
            else:
                return Fraction(int(new_numer), new_denom).reduce_fraction()
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_denom = self.denom * other.denom
            new_numer = self.numer * other.numer
            return Fraction(int(new_numer), new_denom).reduce_fraction()
        else:
            raise ValueError

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_denom = self.denom * other.numer
            new_numer = self.numer * other.denom
            return Fraction(int(new_numer), new_denom).reduce_fraction()
        else:
            raise ValueError

    def reduce_two(self, other):
        return self.reduce_fraction(), other.reduce_fraction()

    def __eq__(self, other):
        first, second = self.reduce_two(other)
        return first.numer == second.numer and first.denom == second.denom

    def __gt__(self, other):
        return self.numer/self.denom > other.numer/other.denom

    def __lt__(self, other):
        return self.numer / self.denom < other.numer / other.denom

    def __ge__(self, other):
        return self.numer / self.denom >= other.numer / other.denom

    def __le__(self, other):
        return self.numer / self.denom <= other.numer / other.denom

    def __str__(self):
        if self.numer % self.denom == 0 and self.numer // self.denom != 0:
            return str(self.numer // self.denom)
        else:
            return f"{self.numer}/{self.denom}"


if __name__ == "__main__":
    f1 = Fraction(9, 6)
    f2 = Fraction(18, 12)
    print(f1 <= f2)
