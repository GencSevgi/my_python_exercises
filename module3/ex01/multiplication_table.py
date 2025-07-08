#!/usr/bin/env python3

def main():
    try:
        num = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
