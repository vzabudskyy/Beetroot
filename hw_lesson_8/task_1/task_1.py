"""
Task 1

Imports practice

 Make a directory with 2 modules; make a function in one of them;
 then import this function in the other module and use that in your script of choice.
"""
from hw_lesson_8.task_1_module import show_list

array_1 = [str(i) for i in range(10)]
array_2 = [[str(i) for i in range(j, j+3)] for j in range(1, 9, 3)]
show_list(array_1)
show_list(array_2, matrix=True)
