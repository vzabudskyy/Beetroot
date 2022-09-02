"""
Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing math operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
```
"""
from calendar import isleap


class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [i**2 for i in nums]

    @staticmethod
    def remove_positives(nums):
        return [num for num in nums if num < 0]

    @staticmethod
    def filter_leaps(dates):
        return[date for date in dates if isleap(date)]

    @staticmethod
    def filter_leaps_wiki(dates):
        result = []
        for date in dates:
            if (date % 4 == 0 and date % 100 != 0) or date % 400 == 0:
                result.append(date)
        return result


if __name__ == "__main__":
    m = Mathematician()
    assert m.filter_leaps_wiki([2021, 2032, 2040, 2100, 2027, 2672]) == [2032, 2040, 2672]
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
    assert m.filter_leaps([2021, 2032, 2040, 2100, 2027, 2400, 2672]) == [2032, 2040, 2400, 2672]
    assert m.filter_leaps_wiki([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
    assert m.filter_leaps_wiki([2021, 2032, 2040, 2100, 2027, 2400, 2672]) == [2032, 2040, 2400, 2672]
