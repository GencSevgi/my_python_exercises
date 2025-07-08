#!/usr/bin/env python3

def main():
    num_str = input("Give me a number: ")
    num = float(num_str)
    # Ondalıklı kısmı sıfırsa integer olarak kabul edelim
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

if __name__ == "__main__":
    main()
