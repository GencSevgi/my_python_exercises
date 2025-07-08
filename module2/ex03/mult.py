#!/usr/bin/env python3

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 * num2

    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is zero.")

    print("num1 * num2 = result")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
