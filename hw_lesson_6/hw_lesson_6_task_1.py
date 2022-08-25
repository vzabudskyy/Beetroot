"""
Task 1

Make a program that has some sentence (a string) on input and returns
a dict containing all unique words as keys and the number of occurrences as values.
"""


raw_string = input("Enter a string:\n")
if " " in raw_string:
    string = raw_string.split(" ")
elif "," in raw_string:
    string = raw_string.split(",")
else:
    string = [raw_string]

"""
Okay, I guess, this check could be realized in better way. Please, give me a feedback about it.
"""
characters = []

for position, word in enumerate(string):
    if not word[-1].isalpha() and not word[-1].isdigit():
        string[position] = word.replace(word[-1], "")
    elif not word[0].isalpha() and not word[0].isdigit():
        string[position] = word.replace(word[0], "")

    string[position] = string[position].lower()

output = {}
for i in string:
    if i not in output:
        output[i] = 1
    else:
        output[i] += 1

for key, value in output.items():
    print(f"{key} : {value}")
