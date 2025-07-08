#!/usr/bin/env python3

def famous_births(figures_dict):
    # Doğum tarihine göre sıralama yapmak için:
    # figures_dict.items() → (key, value) tuple'ları
    # value['date_of_birth'] ile sıralıyoruz (string olarak)
    sorted_figures = sorted(figures_dict.items(), key=lambda item: item[1]['date_of_birth'])
    
    # Sıralanmış her bir kişiyi yazdırıyoruz
    for key, info in sorted_figures:
        print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)
