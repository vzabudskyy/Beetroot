"""
Task2
Написати програму, яка на вхід приймає дату у форматі "1 January 22".
Програма має вивести в консоль дати всіх понеділків в межах даного місяця.
"""
from datetime import datetime, timedelta


def find_all_mondays():
    in_date = input("Enter your date in format '1 January 22':\n")
    user_date = datetime.strptime(in_date, "%d %B %y")

    if user_date.weekday() != 0:
        monday_date = user_date + timedelta(days=7 - user_date.weekday())
    else:
        monday_date = user_date

    while monday_date.month == user_date.month:
        print(f"{monday_date.date()}: {monday_date.strftime('%A')}")
        monday_date += timedelta(days=7)


if __name__ == "__main__":
    while True:
        try:
            find_all_mondays()
            break
        except ValueError:
            print("Input date does not match format, that specified.\n")
