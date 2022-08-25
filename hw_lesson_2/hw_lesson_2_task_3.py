"""
Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""


def calculator(first_num, second_num, operation):
    if operation == "+":
        return first_num + second_num
    elif operation == "-":
        return first_num - second_num
    elif operation == "*":
        return first_num * second_num
    elif operation == "/":
        return first_num / second_num
    elif operation == "^":
        return pow(first_num, second_num)
    elif operation == "abs":
        return abs(first_num)
    elif operation == "//":
        return first_num//second_num
    else:
        return "Incorrect operator"


def main():
    while True:
        op_list = """
                       (+) - Addition
                       (-) - Subtraction
                       (*) - Multiplication
                       (/) - Division
                       (abs) - Modulus
                       (^) - Exponent(power)
                       (//) - Floor division
                       (exit) - Ends of calculations
                       """

        operation = str(input(f"Enter operator from list below:\n {op_list} \n Operator: "))

        if operation == "exit":
            break
        else:
            first_num = int(input("Enter first number:\n"))
            if operation == "abs":
                second_num = 0
            else:
                second_num = int(input("Enter second number:\n"))

        print(calculator(first_num, second_num, operation))


if __name__ == "__main__":
    main()
