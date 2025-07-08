#!/usr/bin/env python3

number = input("Please enter a number: ")
try:
    num = float(number)
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    print("That's not a valid number.")
