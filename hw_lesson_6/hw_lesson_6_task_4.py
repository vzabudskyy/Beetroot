"""
Task 4

Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
"""

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
enumerated_week = {key+1: value for key, value in enumerate(week)}
reversed_enumerated_week = {value: key for key, value in enumerated_week.items()}
print(f"Origin: {enumerated_week}\nReversed: {reversed_enumerated_week}")
