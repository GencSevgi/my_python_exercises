#!/usr/bin/env python3

# İlk mesajı ver
user_input = input("What you gotta say? : ")

# While döngüsü: kullanıcı STOP yazana kadar devam eder
while user_input != "STOP":
    # Cevapla ve tekrar input iste
    user_input = input("I got that! Anything else? : ")

