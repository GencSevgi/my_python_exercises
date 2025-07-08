#!/usr/bin/env python3

# Orijinal array tanımla
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Yeni array oluştur: her elemana 2 ekle
new_array = []
for number in original_array:
    new_array.append(number + 2)

# Her iki array'i ekrana yazdır
print("Original array:", original_array)
print("New array:", new_array)
