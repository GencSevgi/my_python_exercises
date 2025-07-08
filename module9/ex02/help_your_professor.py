#!/usr/bin/env python3

def average(scores_dict):
    # Sözlük değerlerinin toplamını alıyoruz
    total_score = sum(scores_dict.values())
    # Öğrenci sayısını alıyoruz
    number_of_students = len(scores_dict)
    # Ortalama = toplam / öğrenci sayısı
    # Eğer öğrenci sayısı 0 ise sıfıra bölme hatası olmasın diye kontrol
    if number_of_students == 0:
        return 0
    return total_score / number_of_students


if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
