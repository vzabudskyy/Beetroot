"""
Task 2

The sys module.

 The “sys.path” list is initialized from the PYTHONPATH environment variable.
 Is it possible to change it from within Python?
 If so, does it affect where Python looks for module files?
 Run some interactive tests to find it out.
"""
import sys
import os


try:

    [print(f"\t{i}") for i in sys.path]  # let`s look through our PYTHONPATH variable
    from task_1_module import show_list  # after this we will try to import module, that located in the package 'task_1'

except ModuleNotFoundError as ex:
    """
        We will get this error, because interpreter could not find this module
        using paths that were specified in PYTHONPATH variable. So, let`s add
        the path to our package in PYTHONPATH variable over sys.path/
    """

    sys.path.append(os.path.dirname(__file__) + "/1/2/")
    print(4*"\n")

    [print(f"\t{i}") for i in sys.path]  # let`s look through our PYTHONPATH variable again

finally:
    from task_1_module import show_list  # now interpreter will find module and won`t raise an error
    array_1 = [str(i) for i in range(10)]
    show_list(array_1)
    print(os.path.abspath("task_1"))
    print(os.path.dirname(__file__))