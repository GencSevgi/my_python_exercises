#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    for param in args:
        # param 'ism' ile bitiyorsa atla
        # find ile kontrol: 'ism' kelimesinin son 3 karakterde bulunması lazım
        pos = param.find("ism")
        # find 'ism' kelimesini nerede buluyor, -1 ise yok demek
        # ama biz sadece son 3 karakterde olmasına izin vereceğiz
        if pos == len(param) - 3:
            continue  # atla
        print(param + "ism")
