"""
Task 2
Create a python program named "task2", and use the built-in function 'print' in it several times.
Try to pass "sep", "end" params and pass several parameters separated by commas.
Also, provide a comment text above each print statement, mentioned above,
with the expected output after execution of the particular print statement.

(Ex.
# 'hello world'
print("hello world")
)
"""

# This is a sentence
print("This is a sentence")

# This--is--a--sentence--with--separator--and--multiple--parameters
print("This", "is", "a", "sentence", "with", "separator", "and", "multiple", "parameters", sep="--")

"""
This is a sentence...  
...with end parameter
"""
print("This is a sentence...", end=3*"\n")
print("...with end parameter")
