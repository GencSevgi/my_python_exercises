#!/usr/bin/env python3

# Orijinal array
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 5'ten büyük değerlere 2 eklenerek yeni array oluştur
new_array = []
for number in original_array:
    if number > 5:
        new_array.append(number + 2)

# Her iki array'i yazdır (tek satırda, satır sonu boşluk yok)
print(original_array)
print(new_array)

