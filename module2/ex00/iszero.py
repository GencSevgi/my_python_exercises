#!/usr/bin/env python3

number = input("Please enter a number: ")
try:
    num = float(number)
    if num == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("That's not a valid number.")
