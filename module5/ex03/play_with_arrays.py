#!/usr/bin/env python3

# Orijinal array
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 5'ten büyük olanlara 2 ekleyip set'e aktar
new_array = set()
for number in original_array:
    if number > 5:
        new_array.add(number + 2)

# Çıktılar
print(original_array)
print(new_array)
