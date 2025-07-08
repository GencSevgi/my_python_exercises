#!/usr/bin/env python3

def find_the_redheads(family_dict):
    # filter ile sadece "red" saç rengine sahip kişileri seçiyoruz
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    # filter objesini listeye çeviriyoruz ve döndürüyoruz
    return list(redheads)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))
