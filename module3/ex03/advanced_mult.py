#!/usr/bin/env python3

def main():
    num = 0
    while num <= 10:
        print(f"Table of {num}:", end=" ")
        i = 0
        while i <= 10:
            print(num * i, end="")
            if i < 10:
                print(" ", end="")
            i += 1
        print()
        num += 1

if __name__ == "__main__":
    main()
