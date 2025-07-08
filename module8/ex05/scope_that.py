#!/usr/bin/env python3

def add_one(num):
    num += 1
    return num

# Ana program
number = 5
print(number)       # İlk hali

number = add_one(number)  # Fonksiyon çağrısı sonrası değeri güncelle

print(number)       # Fonksiyon sonrası hali
