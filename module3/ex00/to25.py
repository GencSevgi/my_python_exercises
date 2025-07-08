#!/usr/bin/env python3

# Kullanıcıdan input al
print("Enter a number less than 25")
try:
    number = int(input())
except ValueError:
    print("Error")
    exit()

# Sayı 25'ten büyükse hata mesajı ver
if number > 25:
    print("Error")
else:
    # while döngüsü ile 25'e kadar yazdır
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1

