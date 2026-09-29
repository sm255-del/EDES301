# -*- coding: utf-8 -*-

import operator

# Support Python 2 and Python 3
try:
    input = raw_input
except NameError:
    pass

# Global variable mapping operators to functions
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    ">>": operator.rshift,
    "<<": operator.lshift,
    "%": operator.mod,
    "**": operator.pow
}


def get_user_input():
    """Get input from the user."""

    try:
        number1 = input("Enter first number: ")
        operation = input("Enter operator: ")
        number2 = input("Enter second number: ")

        if operation not in operators:
            print("Invalid operator")
            return (None, None, None)

        if operation == ">>" or operation == "<<":
            number1 = int(number1)
            number2 = int(number2)
        else:
            number1 = float(number1)
            number2 = float(number2)

        return (number1, number2, operators[operation])

    except ValueError:
        print("Invalid input")
        return (None, None, None)


if __name__ == "__main__":
    while True:
        number1, number2, function = get_user_input()

        if number1 is None:
            break

        result = function(number1, number2)
        print("Result:", result)
